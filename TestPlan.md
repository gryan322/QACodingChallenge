
# Test Plan - Zero-gen Alert

### Positive Test Cases
* Power is sent as zero, other data continues to be sent, Zero-gen Alert is created, email is sent, Power comes back, alert is cleared, another email indicating cleared Alert is sent.
* Power is sent as zero, other data continues to be sent, Zero-gen Alert is created, email with Alert is sent, Power continues at zero, Alert is not cleared.

### Negative Test Cases
* Power and other data is not being sent, no Zero-gen Alert is created
* Power is not zero, but other data is not being sent, no Zero-gen Alert is created
* Power is sent at non-zero, other data continues to be sent, no Zero-gen Alert is created.

### Subsystem Tests - run as a _functional_ test on notification subsystem
* Message sent to API of notification subsystem that Alert was generated.  Notification subsystem sends Alert email (or sends Alert email to SMTP server) .
  * Date, time, and power plant location of Alert is correct in email
 * Message sent to API of notification subsystem that Alert is cleared.  Notification subsystem send Cleared Alert email.
  * Date, time, power plant location, and current power level is correct in email


### Timing Test
* Power is sent at zero, power immediately (or within a minimum set time) returns to non-zero, Zero-gen Alert is recorded, but no email is sent.

### Security Testing
* Data that would result in Zero-gen Alert cannot be spoofed, or generated easily outside the monitoring system.  Uses authentication to ensure only validated clients are able to input data.
* API for data ingest requires HTTPS to prevent clear text version of data packages from being intercepted.
* Unhandled HTTP methods, (i.e. put, delete) are tested to ensure no unchecked paths to inputting data. 





# Zero-gen Alert Bonus - 
In order to effectively test the Zero Alert with the “sunset” and “sunrise” parameters, I would recommend that an API or Rest endpoint be created that would allow QA to set these parameters on the software being tested.  There should also be an API to validate what they are set to.  Then methods would be added to the automation code to configure these parameters before each test.  If needed, the code that allows these parameters to be set, could be protected to only allow for configuration from the QA environment (via I.P. address range or password).  With the addition of these parameters, these additional test cases would be needed to cover this feature.

* Zero-gen Alert created after “sunset” and before “sunrise” does not get sent or recorded.
* Zero-gen Alert created after “sunrise” but before “sunset” gets sent and recorded.
* Zero-gen Alert created before “sunrise” but not cleared after “sunrise” gets sent and email is sent.
* “Sunrise” parameter that is set later than “sunset” parameter is not allowed.
* “Sunset” parameter this is set before “sunrise” parameter is not allowed.
* Acceptance criteria for when a Zero-gen Alert is created at the time equal to “sunrise” or “sunset” should be established.
