# Challenge 1 Instructions
On a machine with Python 3 installed:
- pip install pytest
- pip install requests

To run tests:
- py.test test_web.py



# QA Coding Challenge
Coding and test plan challenges for QA candidates

# Instructions
- Clone this repo to your local machine
- Use it to create a new repo on GitHub under your own account (please don't use GitHub fork to accomplish this)
- Complete the challenge described below
- Cleanup commit history to have 1 commit per challenge, in order, on the master branch.
- Send us an email with a link to your repo

___
## Challenge 1. Test a static HTML page
Using any python test framework, write a test that makes sure that https://www.google.com/ is up. The goal is not to test the content of the page but rather make sure that the page is available.

* Provide instructions how to run your test. Part of this assignment is to see how you would hand off *production* code to your fellow engineers.
* Your solution will be reviewed by the engineers you would be working with if you joined Also Energy. We are interested in seeing your real-world design, coding, and testing skills.
* If you have any questions, please, email them to the person who sent you the challenge

___
## Challenge 2. Test plan
This challenge is for seasoned QA engineers. If you are applying to a Junior QA Eng position, you are not required to do it.

At Also Energy, we generate all kinds of alerts for the systems that we monitor. Let's think about how to write a test plan for zero generation alerts. This type of alerts is triggered when a monitored system does not produce energy. We still receive the data from the system but the generation number is zero (hence, the name of the alert). When such an alert is created, the user is notified by an email message. When the alert is cleared, the user is notified by email again.

Write a test plan for the system described above. The test plan should cover both alert lifecycle and notification systems. Please, assume that the tests will be automated and could be run anytime during development.

### Bonus
Solar panels don't produce energy at night. Therefore, we had to introduce the configuration parameters `sunset` and `sunrise` that define a time period in the day when we do NOT create zero-gen alerts. Think about how you would test this configuration. Add a couple of test cases to your plan for this feature.
