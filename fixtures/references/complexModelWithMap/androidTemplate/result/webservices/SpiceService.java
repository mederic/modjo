package basepackage_default_value.webservices;

import android.app.Application;

import com.o12s.sampleorganizer.SampleOrganizerApplication;
import com.octo.android.robospice.GoogleHttpClientSpiceService;
import com.octo.android.robospice.persistence.CacheManager;
import com.octo.android.robospice.persistence.exception.CacheCreationException;
import com.octo.android.robospice.persistence.googlehttpclient.json.JacksonObjectPersisterFactory;
import com.octo.android.robospice.request.CachedSpiceRequest;
import com.octo.android.robospice.request.SpiceRequest;
import com.octo.android.robospice.request.listener.RequestListener;

import java.util.ArrayList;
import java.util.Collection;

/**
 * Created by Modjo.
 */
public class SpiceService extends GoogleHttpClientSpiceService {
    private static ArrayList<SpiceRequest> requests = new ArrayList<SpiceRequest>();
    private static ArrayList<RequestListener> listRequestListeners = new ArrayList<RequestListener>();

    @Override
    public CacheManager createCacheManager(Application application) throws CacheCreationException {
        CacheManager cacheManager = new CacheManager();

        // init
        JacksonObjectPersisterFactory jacksonObjectPersisterFactory = new JacksonObjectPersisterFactory(application);

        cacheManager.addPersister(jacksonObjectPersisterFactory);
        return cacheManager;
    }

    @Override
    public void dontNotifyRequestListenersForRequest(CachedSpiceRequest<?> request, Collection<RequestListener<?>> listRequestListener) {
        super.dontNotifyRequestListenersForRequest(request, listRequestListener);
        requests.add(request.getSpiceRequest());
        listRequestListeners.add((RequestListener) listRequestListener.toArray()[0]);
    }

    public static void restartCancelledRequests() {
        for (int i = 0; i != requests.size(); i++) {
            SpiceRequest request = requests.get(i);
            RequestListener requestListener = listRequestListeners.get(i);
            SampleOrganizerApplication.getInstance().getSpiceManager().execute(request, requestListener);
        }
    }
}
