/*
 * Copyright (c) 2010 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */

package basepackage_default_value.webservices;

import com.google.api.client.http.HttpContent;
import com.google.api.client.http.UrlEncodedParser;
import com.google.api.client.util.escape.CharEscapers;

import java.io.IOException;
import java.io.OutputStream;
import java.io.UnsupportedEncodingException;
import java.util.Collection;
import java.util.Collections;
import java.util.Map;

/**
 * Implements support for HTTP form content encoding serialization of type {@code
 * application/x-www-form-urlencoded} as specified in the <a href=
 * "http://www.w3.org/TR/REC-html40/interact/forms.html#h-17.13.4.1">HTML 4.0 Specification</a>.
 * <p/>
 * Sample usage:
 * <p/>
 * <pre>
 * <code>
 * static void setContent(HttpRequest request, Object item) {
 * UrlEncodedContentArraySupport content = new UrlEncodedContentArraySupport();
 * content.data = item;
 * request.content = content;
 * }
 * </code>
 * </pre>
 *
 * @author Yaniv Inbar
 * @since 1.0
 */
public final class UrlEncodedContentArraySupport implements HttpContent {

    /**
     * Content type. Default value is {@link UrlEncodedParser#CONTENT_TYPE}.
     */
    public String contentType = UrlEncodedParser.CONTENT_TYPE;

    /**
     * Key/value data or {@code null} for none.
     */
    public Object data;

    private byte[] content;

    public UrlEncodedContentArraySupport(Object data) {
        super();
        this.data = data;
    }

    public String getEncoding() {
        return null;
    }

    public long getLength() {
        try {
            return computeContent().length;
        } catch (UnsupportedEncodingException e) {
            return 0;
        }
    }

    public String getType() {
        return contentType;
    }

    public void writeTo(OutputStream out) throws IOException {
        out.write(computeContent());
    }

    private byte[] computeContent() throws UnsupportedEncodingException {
        if (content == null) {
            StringBuilder buf = new StringBuilder();
            boolean first = true;
            for (Map.Entry<String, Object> nameValueEntry : mapOf(data).entrySet()) {
                Object value = nameValueEntry.getValue();
                if (value != null) {
                    String name = CharEscapers.escapeUri(nameValueEntry.getKey());
                    if (value instanceof Collection<?>) {
                        Collection<?> collectionValue = (Collection<?>) value;
                        StringBuilder collectionKey;
                        for (Object repeatedValue : collectionValue) {
                            collectionKey = new StringBuilder(name);
                            collectionKey.append("[]");
                            first = appendParam(first, buf, collectionKey.toString(), repeatedValue);
                        }
                    } else if (value.getClass().isArray()) {
                        StringBuilder arrayKey;
                        for (Object repeatedValue : (Object[]) value) {
                            arrayKey = new StringBuilder(name);
                            arrayKey.append("[]");
                            first = appendParam(first, buf, arrayKey.toString(), repeatedValue);
                        }
                    } else {
                        first = appendParam(first, buf, name, value);
                    }
                }
            }
            content = buf.toString().getBytes("UTF-8");
        }
        return content;
    }

    private static boolean appendParam(boolean first, StringBuilder buf, String name, Object value) {
        if (first) {
            first = false;
        } else {
            buf.append('&');
        }
        buf.append(name);
        String stringValue = CharEscapers.escapeUri(value.toString());
        if (stringValue.length() != 0) {
            buf.append('=').append(stringValue);
        }
        return first;
    }

    public boolean retrySupported() {
        return true;
    }

    /**
     * Returns the map to use for the given key/value data.
     *
     * @param data any key value data, represented by an object or a map, or {@code null}
     * @return if {@code data} is a map returns {@code data}; else if {@code data} is {@code null},
     * returns an empty map; else returns null
     */
    public static Map<String, Object> mapOf(Object data) {
        if (data == null) {
            return Collections.emptyMap();
        }
        if (data instanceof Map<?, ?>) {
            @SuppressWarnings("unchecked")
            Map<String, Object> result = (Map<String, Object>) data;
            return result;
        }
        return null;
    }
}