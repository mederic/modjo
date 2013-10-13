add this to build.gradle for robospice dependencies :


dependencies {
        
    compile (group:'com.octo.android.robospice', name:'robospice-google-http-client', version:'1.4.5') {
        exclude group: 'com.google.android'
    }

    compile ('com.google.http-client:google-http-client-jackson:1.15.0-rc') {
        exclude group:'xpp3', module:'xpp3'
        exclude group:'stax', module:'stax-api'
    }

    compile 'org.codehaus.jackson:jackson-mapper-asl:1.9.9'
}