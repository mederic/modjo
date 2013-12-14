package basepackage_default_value.webservices;

import android.app.Application;

import com.octo.android.robospice.GoogleHttpClientSpiceService;
import com.octo.android.robospice.persistence.CacheManager;
import com.octo.android.robospice.persistence.exception.CacheCreationException;
import com.octo.android.robospice.persistence.googlehttpclient.json.JacksonObjectPersisterFactory;


/**
 * Created by Modjo
 */
public class JsonSpiceService extends GoogleHttpClientSpiceService {

    @Override
    public CacheManager createCacheManager(Application application) throws CacheCreationException {
        CacheManager cacheManager = new CacheManager();

        // init
        JacksonObjectPersisterFactory jacksonObjectPersisterFactory = new JacksonObjectPersisterFactory(application);
        cacheManager.addPersister(jacksonObjectPersisterFactory);
        return cacheManager;
    }
}

