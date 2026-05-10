import unittest
import os

import iso20022_new
import exceptions 

MSG_DIR = ".\sample_msgs"

class Test_TSMT(unittest.TestCase):

    def test_049_001_01(self):

        msg_file = os.path.join(MSG_DIR, "sample-tsmt-049-001-01.xml")

        msg = iso20022_new.parse_file(msg_file)

        print(msg)

        """
        self.assertEqual(
            msg.Document.RoleAndBaselnAccptnc.TxId.Id.get(), 
            "Acceptance_Id_sample3"
        )
        self.assertTrue(msg.Document.RoleAndBaselnAccptnc.TxId.validate())

        self.assertEqual(
            msg.Document.RoleAndBaselnAccptnc.AccptncId.CreDtTm.get(),
            "2013-09-28T14:09:00Z"
        )
        self.assertTrue(msg.Document.RoleAndBaselnAccptnc.AccptncId.CreDtTm.validate())

        self.assertEqual(
            msg.Document.RoleAndBaselnAccptnc.RltdMsgRef.CreDtTm.get(),
            "2013-09-28T14:10:00Z"
        )
        self.assertTrue(msg.Document.RoleAndBaselnAccptnc.AccptncId.CreDtTm.validate())

        self.assertTrue(msg.validate())
        """

"""
class Test_PAIN(unittest.TestCase):

    def test_002_001_14(self):

        msg_file = os.path.join(MSG_DIR, "sample-pain-002-001-14.xml")

        good_val = "ACCP"
        bad_val = "Something-invalid"


        msg = parse(msg_file)

        self.assertEqual(
            msg.Document.CstmrPmtStsRpt.OrgnlGrpInfAndSts.GrpSts.get(), 
            good_val
        )
        self.assertTrue(msg.Document.CstmrPmtStsRpt.OrgnlGrpInfAndSts.GrpSts.validate())

        msg.Document.CstmrPmtStsRpt.OrgnlGrpInfAndSts.GrpSts.set(bad_val)

        self.assertEqual(
            msg.Document.CstmrPmtStsRpt.OrgnlGrpInfAndSts.GrpSts.get(), 
            bad_val
        )
        self.assertRaises(
            exceptions.ValidateError,
            msg.Document.CstmrPmtStsRpt.OrgnlGrpInfAndSts.GrpSts.validate
        )
        self.assertRaises(
            exceptions.ValidateError,
            msg.validate
        )

        msg.Document.CstmrPmtStsRpt.OrgnlGrpInfAndSts.GrpSts.set(good_val)

        self.assertEqual(
            msg.Document.CstmrPmtStsRpt.OrgnlGrpInfAndSts.GrpSts.get(), 
            good_val
        )
        self.assertTrue(msg.Document.CstmrPmtStsRpt.OrgnlGrpInfAndSts.GrpSts.validate())
        self.assertTrue(msg.validate())

"""

if __name__ == "__main__":
    unittest.main()
