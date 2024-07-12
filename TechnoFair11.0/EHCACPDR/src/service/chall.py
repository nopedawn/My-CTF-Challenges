import random
import sys

questions = [
    "As you begin your investigation, you notice the system's foundation. What operating system is this machine running? e.g. (XXX_XXX)",
    "Every user leaves a trace. In this case, what Username stands out in the logs?",
    "The first login can often reveal crucial timing. When did our person of interest first access the system? e.g. (h:mm_MM/DD/YYYY)",
    "Remote access is key in many operations. What specific software did the user employ for remote computer connections?",
    "Cloud configurations can pinpoint locations. When setting up the instance, which gcloud zone was specified? e.g. (XXX-XXX-XXX)",
    "Tunnels are often used for secure connections. What port number did the user attempt to use when starting the IAP tunnel?",
    "A successful login provides an overview of the user's identity and location. Upon connecting via PuTTY, what username and hostname combination appeared? e.g. (username@hostname)",
    "Security keys are a treasure trove of information. Can you provide the exact path where the ssh keys are stored on this system?",
    "Rumors of malware often turn out to be misunderstood legitimate processes. A program running in the background has sparked discussion in forums about potential spyware, but it's actually a standard Windows component. Can you identify this often-misunderstood process? e.g. (XXX_XXX_XXX)",
    "Organization is crucial in any system. In our final observation, how many server groups did you identify in total?"
]

answers = [
    "Windows_10",
    "student_01_dc0fa1dd7",
    "2:06_3/12/2024",
    "PuTTY",
    "us-west1-c",
    "3389",
    "sa_115757880695163405973@linux-iap",
    r"C:\Users\student_01_dc0fa1dd7\.ssh",
    "Windows_Command_Processor",
    "1"
]

flag = "TechnoFair11{RDP_C4CH3_0B53RV3R_FRFRFR}"

def challenge():
    print("Let's interrogate what you've discovered.")
    print("(If there are spaces, it can be replaced with `_` (underscore))\n")

    try:
        while True:
            ready = input("Are you ready to start? (Y/n): ").strip().lower()
            if ready == 'y' or ready == '':
                print()
                break
            elif ready == 'n':
                print()
                sys.exit(0)
            else:
                print("Invalid input. Please enter 'Y' or 'n'.")
    except KeyboardInterrupt:
        print("\nAborted!")
        sys.exit(0)

    try:
        for i in range(len(questions)):
            print(f"{i+1}. {questions[i]}")
            user_answer = input("Answer: ").strip()
            if user_answer.lower() == answers[i].lower():
                print("Correct!")
            else:
                print("Wrong!! BLEHHHHH :P\n")
                sys.exit(1)
            print()

        print("Well done!")
        print(f"Here's your flag: {flag}")
    except KeyboardInterrupt:
        print("\nAborted!")
        sys.exit(0)

if __name__ == "__main__":
    challenge()