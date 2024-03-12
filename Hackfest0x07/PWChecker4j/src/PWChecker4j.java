//package pwchecker4j;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class PWChecker4j extends JFrame {
    private static final char[] alp = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ".toCharArray();
    private static final String urCheckPoints = new String(new char[]{
            alp[15], alp[77], alp[18], alp[62], alp[15], alp[83],
            alp[39], alp[18], alp[81], alp[62], alp[83], alp[56],
            alp[79], alp[18], alp[62], alp[15], alp[69], alp[62],
            alp[81], alp[18], alp[85], alp[18], alp[49], alp[20],
            alp[16], alp[77], alp[24], alp[62], alp[16], alp[20],
            alp[62], alp[73], alp[19], alp[85], alp[19]
    });

    private static final String mainMSG = new String(new char[]{
            alp[36], alp[77], alp[83], alp[68], alp[81], alp[94], alp[83],
            alp[71], alp[68], alp[94], alp[79], alp[64], alp[82], alp[82],
            alp[86], alp[78], alp[81], alp[67], alp[0], alp[94], alp[7],
            alp[36], alp[94], alp[83], alp[78], alp[94], alp[36], alp[87],
            alp[72], alp[83], alp[8], alp[25], alp[94]
    });

    private static final String msg1 = new String(new char[]{
            alp[51], alp[71], alp[64], alp[83], alp[6], alp[82],
            alp[94], alp[72], alp[83], alp[0], alp[94]
    });

    private static final String msg2 = new String(new char[]{
            alp[77], alp[78], alp[94], alp[76], alp[78], alp[81], alp[68], alp[94],
            alp[69], alp[75], alp[64], alp[70], alp[94], alp[69], alp[78],
            alp[81], alp[94], alp[88], alp[78], alp[84], alp[94], alp[25],
            alp[79], alp[94]
    });

    private static final String sys0 = new String(new char[]{
            alp[54], alp[81], alp[78], alp[77], alp[70], alp[0], alp[94]
    });

    private static final String fmt1 = new String(new char[]{
            alp[37], alp[75], alp[64], alp[70], alp[25], alp[94], alp[39], alp[64], alp[66], alp[74],
            alp[69], alp[68], alp[82], alp[83], alp[15], alp[87], alp[15], alp[22], alp[90]
    });
    private static final String fmt2 = new String(new char[]{
            alp[92], alp[94]
    });

    public PWChecker4j() {
        super("PWChecker4j");

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //setSize(400, 150);
	    setSize(350, 200);
        setResizable(false);
        setLayout(new BorderLayout());

        JTextField textField = new JTextField(20); // Adjusted width
        JButton submitButton = new JButton("Submit");

        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String userInput = textField.getText().trim();

                if (userInput.equals(urCheckPoints)) {
                    JOptionPane.showMessageDialog(PWChecker4j.this, msg1 + "\n" + fmt1 + urCheckPoints + fmt2);
                    System.exit(0);
                } else if (userInput.equals("" + alp[36])) {
                    JOptionPane.showMessageDialog(PWChecker4j.this, msg2);
                    System.exit(0);
                } else {
                    JOptionPane.showMessageDialog(PWChecker4j.this, sys0);
                }
            }
        });

        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());
        panel.add(new JLabel(mainMSG));
        panel.add(textField);
        panel.add(submitButton);

        add(panel, BorderLayout.CENTER);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new PWChecker4j().setVisible(true);
            }
        });
    }
}


