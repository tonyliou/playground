/* ESP32 AWS IoT
 *  
 * Simplest possible example (that I could come up with) of using an ESP32 with AWS IoT.
 *  
 * Author: Anthony Elder 
 * License: Apache License v2
 */
#include <WiFiClientSecure.h>
#include <PubSubClient.h> // install with Library Manager, I used v2.6.0

const char* ssid = "inc";
const char* password = "inc811008";

const char* awsEndpoint = "a1gubz9fjm577v-ats.iot.ap-northeast-1.amazonaws.com";

// Update the two certificate strings below. Paste in the text of your AWS 
// device certificate and private key. Add a quote character at the start
// of each line and a backslash, n, quote, space, backslash at the end 
// of each line:

// xxxxxxxxxx-certificate.pem.crt
const char* certificate_pem_crt = \
"-----BEGIN CERTIFICATE-----\n" \
"MIIDWTCCAkGgAwIBAgIUSDVgWTt2f3BDFlbX7IbD/sL1zowwDQYJKoZIhvcNAQEL\n" \
"BQAwTTFLMEkGA1UECwxCQW1hem9uIFdlYiBTZXJ2aWNlcyBPPUFtYXpvbi5jb20g\n" \
"SW5jLiBMPVNlYXR0bGUgU1Q9V2FzaGluZ3RvbiBDPVVTMB4XDTIxMDcwMjAxNDAx\n" \
"MloXDTQ5MTIzMTIzNTk1OVowHjEcMBoGA1UEAwwTQVdTIElvVCBDZXJ0aWZpY2F0\n" \
"ZTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALaN5/im5EqrOlBM80oU\n" \
"Ec/2xHBNGKLXq5zWoaMdqF0PF5SgDHwDMJ64hMEQ6KZDXGS3eBZUXHhG6A61KBoT\n" \
"uIPlZ39f0Rp/FtWNs8UFDpabtYpAGd4KyTn1gx0a3bZ1e0DoVq5EHGjT9lWPMDfM\n" \
"VDLgFEJ61+nfwBpLZ12V/M6g9FG7PrcHUU4xzVjvXvOyZjlggQwtuflFCoaZBlv2\n" \
"h9s7ONPfyuB9lvnvLHApa8aLEitgf38Q9uOSLI1ympLrgADU4595tqB+rCqd0/Mx\n" \
"4vO2FsOyY0ZhH2mEAxd9Qw/acNhmymCMprlAWocJx3WT4wxmn2wzuBWsfjGWjjKw\n" \
"pOcCAwEAAaNgMF4wHwYDVR0jBBgwFoAUi7vezMfIBs2r/HP3LunkTRPAfmMwHQYD\n" \
"VR0OBBYEFNXDcYzPgNbmEkeSChs3G8MCg2tkMAwGA1UdEwEB/wQCMAAwDgYDVR0P\n" \
"AQH/BAQDAgeAMA0GCSqGSIb3DQEBCwUAA4IBAQBsq7NITJxLsOyVJJASkYsylB/Y\n" \
"l+cu2CjZrxRkjPFJ31b9o0fHqOmvfI6hCaywz7DchMMU9I3RxOuCfzsXmocbbRaC\n" \
"7W/XJDN8+h3k6ZVQ14xg1eQX2HpTzl/4DLiAX3rX/1Q70jtd0dQ4iaTQuTQfVExu\n" \
"kAZRSmsft3k/HdPefxgLn4p7SgveD4CWcQcbRdlw4zSeNrgKXMPttwjfk0M0jTUZ\n" \
"gHevDdIyREnQ6SZWh05M8KTQ2xXtRqv2LuaaZTnIN0pgVoMOg96fJ+rDCOboYBGa\n" \
"J+kf0m4ybcez/LbXFYIklK+cIuGa3n6BUfGLa+C5gYhPK2zpxlmOR2vb3fWo\n" \
"-----END CERTIFICATE-----\n";

// xxxxxxxxxx-private.pem.key
const char* private_pem_key = \
"-----BEGIN RSA PRIVATE KEY-----\n" \
"MIIEowIBAAKCAQEAto3n+KbkSqs6UEzzShQRz/bEcE0YoternNahox2oXQ8XlKAM\n" \
"fAMwnriEwRDopkNcZLd4FlRceEboDrUoGhO4g+Vnf1/RGn8W1Y2zxQUOlpu1ikAZ\n" \
"3grJOfWDHRrdtnV7QOhWrkQcaNP2VY8wN8xUMuAUQnrX6d/AGktnXZX8zqD0Ubs+\n" \
"twdRTjHNWO9e87JmOWCBDC25+UUKhpkGW/aH2zs409/K4H2W+e8scClrxosSK2B/\n" \
"fxD245IsjXKakuuAANTjn3m2oH6sKp3T8zHi87YWw7JjRmEfaYQDF31DD9pw2GbK\n" \
"YIymuUBahwnHdZPjDGafbDO4Fax+MZaOMrCk5wIDAQABAoIBAFGw2OB1Vm1viC3M\n" \
"8YXxyzLD243hgifE2R/bEAPdTq0uBsBUiqGoD8bHDWkT9vgH5r2POGbNo3+TQ17p\n" \
"hCN/Na+YJaNjLkBsJLy1p39/ztJopWlTW//31aphCiYpEpQGqHwYPEnJYukqCO6q\n" \
"n8ooXnlRut8w95PJs75QhdXkO3f+3qxJ9bVqwr+mzyZw6uDpm38BHkWJ+OKovgj3\n" \
"ug7EHuA/YOicyweZLQqif/AG+RFGBeexm8KSTkopa8icvDw27mBRM+7nFDPtSIdd\n" \
"qAoBn3XTXGLnfiZEKmscjGyo/5CFY16MruRDUDS1X82KxUy/8cCmiGGdl1RrW3oJ\n" \
"3jj0dGECgYEA6T/fu29OsGNQwU1z9cz6XoWYVjIopTYgtrMzR/bXmRVJyixXwvqZ\n" \
"P5dfSP/BlUWf0jDQUabfqntRuS3hCRla/6JhsjOJbihSG1WUo9qySnnBxMB5DGNZ\n" \
"xgn3UZri1dO33uFoKlmeyj2j5ggVtq+10kaGLmbESHZKcXQn8+/yWtcCgYEAyFwy\n" \
"vA0iv1x3fLFEAQXJylS5iO//a8BlPXkR+EPX/nTP5Lme6/zLpBb69I1nl7ipnSOI\n" \
"i7vW9i0xW8K6MfGCpt7/zNWqgo/aH6TtigJLXW/q2ymtTkgwK14/zV2nmNdbefyC\n" \
"0MweeEfZ1YMzELLTt5K/YAquh+X2Aog5jZ9YVHECgYEAwQoTAU4Cgur/J6wRX4mw\n" \
"YFASnqvOhcUBWBOBSnrZPiGnO0Jts7mw4TdHLeQ1c3P27H9nuVvxWmfLYAW/a8dn\n" \
"T5A1aMVMZTXLlkHCzcUur4KLQmnFBOKopsUSwZ/9QdiCIVzN19bqGxjer39bcSGE\n" \
"yi2B2Z9FrW7w92qZskKQgmsCgYAus67vvnAXAsqnOfqL8nlyvATzMl3rE9GFXq8d\n" \
"m1LBcSD0Q4ATqb0d5m1gi4VWDCkdA6dUSth0UVxr8xvLgGvf0aL2b+dqv3UsYxkr\n" \
"ThWbFfc8Vp6a3KC9ux5MFER4j9o2uPEVEj8X8keISSih/8zxwTbygArmimepd29S\n" \
"342LQQKBgCPtzag9QkMmpI8I+sLAuaF9aPQdY8GvxSLKuom93Yw2LQ+lt1Se+AP2\n" \
"XoHdHnaWETEHeNlzMVujmkYL6t0ajafLn2Kt1zaDwAnl+yik+ZdwKEJcKtNyJk8B\n" \
"bBiH0fuWYxFywkKXQ7iM2YBUr4ukF4A3d+tklVRE+1BWnk4ad0kI\n" \
"-----END RSA PRIVATE KEY-----\n";


/* root CA can be downloaded in:
  https://www.symantec.com/content/en/us/enterprise/verisign/roots/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem
*/
const char* rootCA = \
"-----BEGIN CERTIFICATE-----\n" \
"MIIDQTCCAimgAwIBAgITBmyfz5m/jAo54vB4ikPmljZbyjANBgkqhkiG9w0BAQsF\n" \
"ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6\n" \
"b24gUm9vdCBDQSAxMB4XDTE1MDUyNjAwMDAwMFoXDTM4MDExNzAwMDAwMFowOTEL\n" \
"MAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEZMBcGA1UEAxMQQW1hem9uIFJv\n" \
"b3QgQ0EgMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALJ4gHHKeNXj\n" \
"ca9HgFB0fW7Y14h29Jlo91ghYPl0hAEvrAIthtOgQ3pOsqTQNroBvo3bSMgHFzZM\n" \
"9O6II8c+6zf1tRn4SWiw3te5djgdYZ6k/oI2peVKVuRF4fn9tBb6dNqcmzU5L/qw\n" \
"IFAGbHrQgLKm+a/sRxmPUDgH3KKHOVj4utWp+UhnMJbulHheb4mjUcAwhmahRWa6\n" \
"VOujw5H5SNz/0egwLX0tdHA114gk957EWW67c4cX8jJGKLhD+rcdqsq08p8kDi1L\n" \
"93FcXmn/6pUCyziKrlA4b9v7LWIbxcceVOF34GfID5yHI9Y/QCB/IIDEgEw+OyQm\n" \
"jgSubJrIqg0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMC\n" \
"AYYwHQYDVR0OBBYEFIQYzIU07LwMlJQuCFmcx7IQTgoIMA0GCSqGSIb3DQEBCwUA\n" \
"A4IBAQCY8jdaQZChGsV2USggNiMOruYou6r4lK5IpDB/G/wkjUu0yKGX9rbxenDI\n" \
"U5PMCCjjmCXPI6T53iHTfIUJrU6adTrCC2qJeHZERxhlbI1Bjjt/msv0tadQ1wUs\n" \
"N+gDS63pYaACbvXy8MWy7Vu33PqUXHeeE6V/Uq2V8viTO96LXFvKWlJbYK8U90vv\n" \
"o/ufQJVtMVT8QtPHRh8jrdkPSHCa2XV4cdFyQzR1bldZwgJcJmApzyMZFo6IQ6XU\n" \
"5MsI+yMRQ+hDKXJioaldXgjUkK642M4UwtBV8ob2xJNDd2ZhwLnoQdeXeGADbkpy\n" \
"rqXRfboQnoZsG4q5WTP468SQvvG5\n" \
"-----END CERTIFICATE-----\n";


WiFiClientSecure wiFiClient;
void msgReceived(char* topic, byte* payload, unsigned int len);
PubSubClient pubSubClient(awsEndpoint, 8883, msgReceived, wiFiClient); 

void setup() {
  Serial.begin(115200); delay(50); Serial.println();
  Serial.println("ESP32 AWS IoT Example");
  Serial.printf("SDK version: %s\n", ESP.getSdkVersion());

  Serial.print("Connecting to "); Serial.print(ssid);
  WiFi.begin(ssid, password);
  WiFi.waitForConnectResult();
  Serial.print(", WiFi connected, IP address: "); Serial.println(WiFi.localIP());

  wiFiClient.setCACert(rootCA);
  wiFiClient.setCertificate(certificate_pem_crt);
  wiFiClient.setPrivateKey(private_pem_key);
}

unsigned long lastPublish;
int msgCount;

void loop() {

  pubSubCheckConnect();

  if (millis() - lastPublish > 10000) {
    String msg = String("Hello from ESP32: ") + ++msgCount;
    boolean rc = pubSubClient.publish("Aking/ESP32/000001/information", msg.c_str());
    Serial.print("Published, rc="); Serial.print( (rc ? "OK: " : "FAILED: ") );
    Serial.println(msg);
    lastPublish = millis();
  }
}

void msgReceived(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message received on "); Serial.print(topic); Serial.print(": ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void pubSubCheckConnect() {
  if ( ! pubSubClient.connected()) {
    Serial.print("PubSubClient connecting to: "); Serial.print(awsEndpoint);
    while ( ! pubSubClient.connected()) {
      Serial.print(".");
      pubSubClient.connect("ESPthingXXXX");
      delay(1000);
    }
    Serial.println(" connected");
    pubSubClient.subscribe("Aking/ESP32/000001/command");
  }
  pubSubClient.loop();
}
