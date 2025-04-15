![Banner](images/banner.png)

![Banner](../logo/banner.png)

<details>
<summary>🧭 Quick navigation links </summary>

* [Overview](#overview)
* [Quickstart](#quickstart)
    * [Message parsing](#message-parsing)
    * [Message editing](#message-editing)
    * [Message validation](#message-validation)
    * [Message generation](#message-generation)
    * [Message serialisation/deserialisation](#message-serialisationdeserialisation)
* [Supported message classes](#supported-message-classes)

</details>

## Overview

The **ISO20022 Playset** is a swiss army knife for experimentation with ISO20022 messages. It's designed to be easy and intuitive to use, and aims to get your ISO20022 projects up and running as quickly as possible.

Here are some things it can do out of the box:

* **Parse messages**: Messages can be parsed from a variety of sources.
* **Create and modify messages**: Messages can be created with user-supplied data, or fields in existing messages can be modified.
* **Validate messages**: Messages can be validated against the ISO20022 schema.
* **Generate sample messages**: Schema-compliant messages of a specified type can be generated with synthetic data.
* **Serialise and deserialise messages**: *coming soon!*

## Quickstart

### Message parsing

#### Parse from file

```python
path_to_xml = os.path.join(".", "sample_msgs", "sample-tsmt-049-001-01.xml")
isomsg = iso20022.parse_file(path_to_xml)
print(type(isomsg))
```

#### Parse from string

```python
xml_string = """
    <Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.002.001.14">
        <CstmrPmtStsRpt>
            <GrpHdr>
                <MsgId>ABC123</MsgId>
                <CreDtTm>1970-01-01T12:00:00</CreDtTm>
            </GrpHdr>
            <OrgnlGrpInfAndSts>
                <OrgnlMsgId>XYZ456</OrgnlMsgId>
                <OrgnlMsgNmId>pain.001.001.03</OrgnlMsgNmId>
            </OrgnlGrpInfAndSts>
        </CstmrPmtStsRpt>
    </Document>
"""
isomsg = iso20022.parse_xml(xml_string)
print(type(isomsg))
```

#### Parse from ElementTree

```python
import defusedxml.ElementTree as ET

path_to_xml = os.path.join(".", "sample_msgs", "sample-tsmt-049-001-01.xml")
tree = ET.parse(path_to_xml)
isomsg = iso20022.parse_etree(tree)
print(type(isomsg))
```

#### Read specfic fields
```python
path_to_xml = os.path.join(".", "sample_msgs", "sample-tsmt-049-001-01.xml")
isomsg = iso20022.parse_file(path_to_xml)
print(isomsg.RoleAndBaselnAccptnc.TxId.Id.get())

```

### Message editing

#### Create message from stratch

```python
isomsg = iso20022.PAIN_002_001_14.Document("Document")

isomsg.CstmrPmtStsRpt = iso20022.CustomerPaymentStatusReportV14("CstmrPmtStsRpt")
isomsg.CstmrPmtStsRpt.GrpHdr = iso20022.GroupHeader128("GrpHdr")
isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts = iso20022.OriginalGroupHeader22("OrgnlGrpInfAndSts")

isomsg.CstmrPmtStsRpt.GrpHdr.MsgId = iso20022.Max35Text("MsgId")
isomsg.CstmrPmtStsRpt.GrpHdr.MsgId.set("Example header msgid")

isomsg.CstmrPmtStsRpt.GrpHdr.CreDtTm = iso20022.ISODateTime("CreDtTm")
isomsg.CstmrPmtStsRpt.GrpHdr.CreDtTm.set("1970-01-01T12:00:00")

isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgId = iso20022.Max35Text("OrgnlMsgId")
isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgId.set("Example original msgid")

isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgNmId = iso20022.Max35Text("OrgnlMsgNmId")
isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgNmId.set("pain.001.001.02")

print(isomsg.to_xml())
```

#### Update message field

```python
xml_string = """
    <Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.029.001.13">
        <RsltnOfInvstgtn>
            <Assgnmt>
                <Id>RES123</Id>
                <Assgnr>
                    <Pty>
                        <Nm>AssigningBank</Nm>
                    </Pty>
                </Assgnr>
                <Assgne>
                    <Pty>
                        <Nm>ReceivingBank</Nm>
                    </Pty>
                </Assgne>
                <CreDtTm>1970-01-01T12:00:00</CreDtTm>
            </Assgnmt>
            <Sts>
                <RjctdMod>
                    <Prtry>
                        ExampleString
                    </Prtry>
                </RjctdMod>
            </Sts>
        </RsltnOfInvstgtn>
    </Document>
"""
isomsg = iso20022.parse_xml(xml_string)
isomsg.RsltnOfInvstgtn.Sts.RjctdMod[0].Prtry.set("Some other string")
print(isomsg.to_xml())

```

### Message validation

```python

xml_string = """
    <Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.029.001.13">
        <RsltnOfInvstgtn>
            <Assgnmt>
                <Id>RES123</Id>
                <Assgnr>
                    <Pty>
                        <Nm>AssigningBank</Nm>
                    </Pty>
                </Assgnr>
                <Assgne>
                    <Pty>
                        <Nm>ReceivingBank</Nm>
                    </Pty>
                </Assgne>
                <CreDtTm>1970-01-01T12:00:00</CreDtTm>
            </Assgnmt>
            <Sts>
                <RjctdMod>
                    <Prtry>
                        ExampleString
                    </Prtry>
                </RjctdMod>
            </Sts>
        </RsltnOfInvstgtn>
    </Document>
"""
isomsg = iso20022.parse_xml(xml_string)
isomsg.validate()

# Can detect invalid messages
isomsg.RsltnOfInvstgtn.Assgnmt.Id.set("A"*36) # This is a Max35Text field
try:
    isomsg.validate()
except iso20022.ValidateError as e:
    print(f"{str(e)}")

# Can validate whole message, or just individual sections or entries
isomsg.RsltnOfInvstgtn.Sts.validate()
isomsg.RsltnOfInvstgtn.Sts.RjctdMod[0].Prtry.validate()

```

### Message generation

```python

# Generate messages of a given type.
isomsg = iso20022.TSMT_049_001_01.Document("Document")
for _ in range(3):
    isomsg.generate()
    print(isomsg.to_xml())

```

### Message serialisation/deserialisation

*Coming soon!*


## Supported message classes

The **ISO20022 Playset** supports the following message classes:

<details>
<summary><b>ACMT</b> (Account Management)</summary>

* acmt.001.001.08
* acmt.002.001.08
* acmt.003.001.08
* acmt.005.001.06
* acmt.006.001.07
* acmt.007.001.05
* acmt.008.001.05
* acmt.009.001.04
* acmt.010.001.04
* acmt.011.001.04
* acmt.012.001.04
* acmt.013.001.04
* acmt.014.001.05
* acmt.015.001.04
* acmt.016.001.04
* acmt.017.001.04
* acmt.018.001.04
* acmt.019.001.04
* acmt.020.001.04
* acmt.021.001.04
* acmt.022.001.04
* acmt.023.001.04
* acmt.024.001.04
* acmt.027.001.05
* acmt.028.001.05
* acmt.029.001.05
* acmt.030.001.04
* acmt.031.001.05
* acmt.032.001.05
* acmt.033.001.02
* acmt.034.001.05
* acmt.035.001.02
* acmt.036.001.01
* acmt.037.001.02

</details>

<details>
<summary><b>ADMI</b> (Administration)</summary>

* admi.004.001.02
* admi.005.001.02
* admi.006.001.01
* admi.007.001.01
* admi.024.001.01

</details>

<details>
<summary><b>AUTH</b> (Authorities)</summary>

* auth.001.001.02
* auth.002.001.02
* auth.003.001.01
* auth.012.001.02
* auth.013.001.02
* auth.014.001.02
* auth.015.001.02
* auth.016.001.03
* auth.017.001.02
* auth.018.001.04
* auth.019.001.04
* auth.020.001.04
* auth.021.001.04
* auth.022.001.04
* auth.023.001.04
* auth.024.001.04
* auth.025.001.04
* auth.026.001.04
* auth.027.001.04
* auth.028.001.01
* auth.029.001.05
* auth.030.001.04
* auth.031.001.01
* auth.032.001.01
* auth.033.001.03
* auth.034.001.01
* auth.035.001.01
* auth.036.001.03
* auth.038.001.01
* auth.039.001.01
* auth.040.001.01
* auth.041.001.01
* auth.042.001.02
* auth.043.001.01
* auth.044.001.02
* auth.045.001.03
* auth.047.001.01
* auth.048.001.01
* auth.049.001.02
* auth.050.001.01
* auth.052.001.02
* auth.053.001.01
* auth.054.001.01
* auth.055.001.01
* auth.056.001.01
* auth.057.001.02
* auth.058.001.01
* auth.059.001.02
* auth.060.001.02
* auth.061.001.02
* auth.062.001.01
* auth.063.001.01
* auth.064.001.02
* auth.065.001.01
* auth.066.001.01
* auth.067.001.01
* auth.068.001.01
* auth.069.001.02
* auth.070.001.02
* auth.071.001.02
* auth.072.001.01
* auth.076.001.01
* auth.077.001.01
* auth.078.001.02
* auth.079.001.02
* auth.080.001.02
* auth.083.001.02
* auth.084.001.02
* auth.085.001.02
* auth.086.001.02
* auth.090.001.02
* auth.091.001.03
* auth.092.001.04
* auth.094.001.02
* auth.100.001.01
* auth.101.001.01
* auth.102.001.01
* auth.105.001.01
* auth.106.001.01
* auth.107.001.02
* auth.108.001.02
* auth.109.001.02
* auth.112.001.01
* auth.113.001.01

</details>

<details>
<summary><b>CAAA</b> (Acceptor to Acquirer Card Transactions)</summary>

* caaa.001.001.14
* caaa.002.001.14
* caaa.003.001.14
* caaa.004.001.13
* caaa.005.001.14
* caaa.006.001.13
* caaa.007.001.14
* caaa.008.001.13
* caaa.009.001.13
* caaa.010.001.12
* caaa.011.001.14
* caaa.012.001.13
* caaa.013.001.13
* caaa.014.001.12
* caaa.015.001.06
* caaa.016.001.12
* caaa.017.001.12
* caaa.018.001.09
* caaa.019.001.08
* caaa.020.001.06
* caaa.021.001.06
* caaa.022.001.05
* caaa.023.001.05
* caaa.024.001.05
* caaa.025.001.05
* caaa.026.001.02
* caaa.027.001.02

</details>

<details>
<summary><b>CAAD</b> (Card Administration)</summary>

* caad.001.001.03
* caad.002.001.03
* caad.003.001.03
* caad.004.001.03
* caad.005.001.04
* caad.006.001.04
* caad.007.001.04
* caad.008.001.02
* caad.009.001.02
* caad.010.001.02

</details>

<details>
<summary><b>CAAM</b> (ATM Management)</summary>

* caam.001.001.04
* caam.002.001.04
* caam.003.001.04
* caam.004.001.04
* caam.005.001.03
* caam.006.001.02
* caam.007.001.01
* caam.008.001.01
* caam.009.001.03
* caam.010.001.03
* caam.011.001.02
* caam.012.001.02
* caam.013.001.01
* caam.014.001.01
* caam.015.001.01
* caam.016.001.01

</details>

<details>
<summary><b>CAFC</b> (Fee Collection)</summary>

* cafc.001.001.03
* cafc.002.001.03

</details>

<details>
<summary><b>CAFM</b> (File Management)</summary>

* cafm.001.001.03
* cafm.002.001.03

</details>

<details>
<summary><b>CAFR</b> (Fraud Reporting and Disposition)</summary>

* cafr.001.001.03
* cafr.002.001.03
* cafr.003.001.03
* cafr.004.001.03

</details>

<details>
<summary><b>CAIN</b> (Acquirer to Issuer Card Transactions)</summary>

* cain.001.001.04
* cain.002.001.04
* cain.003.001.04
* cain.004.001.04
* cain.005.001.04
* cain.006.001.04
* cain.014.001.03
* cain.015.001.03
* cain.016.001.03
* cain.017.001.03
* cain.018.001.03
* cain.019.001.03
* cain.020.001.03
* cain.021.001.03
* cain.022.001.03
* cain.023.001.03
* cain.024.001.03
* cain.025.001.03
* cain.026.001.03
* cain.027.001.03
* cain.028.001.03

</details>

<details>
<summary><b>CAMT</b> (Cash Management)</summary>

* camt.003.001.08
* camt.004.001.10
* camt.005.001.11
* camt.006.001.11
* camt.007.001.10
* camt.008.001.11
* camt.009.001.08
* camt.010.001.09
* camt.011.001.08
* camt.012.001.08
* camt.013.001.04
* camt.014.001.05
* camt.015.001.04
* camt.016.001.04
* camt.017.001.05
* camt.018.001.05
* camt.019.001.07
* camt.020.001.04
* camt.021.001.06
* camt.023.001.07
* camt.024.001.08
* camt.025.001.09
* camt.026.001.10
* camt.027.001.10
* camt.028.001.12
* camt.029.001.13
* camt.030.001.06
* camt.031.001.07
* camt.032.001.05
* camt.033.001.07
* camt.034.001.07
* camt.035.001.06
* camt.036.001.06
* camt.037.001.10
* camt.038.001.05
* camt.039.001.06
* camt.040.001.04
* camt.041.001.04
* camt.042.001.04
* camt.043.001.04
* camt.044.001.03
* camt.045.001.03
* camt.046.001.08
* camt.047.001.08
* camt.048.001.07
* camt.049.001.07
* camt.050.001.07
* camt.051.001.07
* camt.052.001.13
* camt.053.001.13
* camt.054.001.13
* camt.055.001.12
* camt.056.001.11
* camt.057.001.08
* camt.058.001.09
* camt.059.001.08
* camt.060.001.07
* camt.061.001.02
* camt.062.001.03
* camt.063.001.02
* camt.064.001.01
* camt.065.001.01
* camt.066.001.02
* camt.067.001.02
* camt.068.001.02
* camt.069.001.05
* camt.070.001.06
* camt.071.001.05
* camt.072.001.02
* camt.073.001.02
* camt.074.001.02
* camt.075.001.02
* camt.078.001.02
* camt.079.001.02
* camt.080.001.02
* camt.081.001.02
* camt.082.001.02
* camt.083.001.02
* camt.084.001.02
* camt.085.001.02
* camt.086.001.05
* camt.087.001.09
* camt.088.001.03
* camt.101.001.02
* camt.102.001.03
* camt.103.001.03
* camt.104.001.01
* camt.105.001.03
* camt.106.001.03
* camt.107.001.02
* camt.108.001.02
* camt.109.001.02
* camt.110.001.01
* camt.111.001.02

</details>

<details>
<summary><b>CANM</b> (Network Management)</summary>

* canm.001.001.04
* canm.002.001.04
* canm.003.001.04
* canm.004.001.04

</details>

<details>
<summary><b>CASP</b> (Sale to POI Card Transactions)</summary>

* casp.001.001.07
* casp.002.001.07
* casp.003.001.07
* casp.004.001.07
* casp.005.001.07
* casp.006.001.07
* casp.007.001.07
* casp.008.001.07
* casp.009.001.07
* casp.010.001.07
* casp.011.001.07
* casp.012.001.07
* casp.013.001.02
* casp.014.001.07
* casp.015.001.07
* casp.016.001.07
* casp.017.001.07

</details>

<details>
<summary><b>CASR</b> (Settlement Reporting)</summary>

* casr.001.001.03
* casr.002.001.03

</details>

<details>
<summary><b>CATM</b> (Terminal Management)</summary>

* catm.001.001.14
* catm.002.001.13
* catm.003.001.14
* catm.004.001.05
* catm.005.001.11
* catm.006.001.08
* catm.007.001.07
* catm.008.001.07

</details>

<details>
<summary><b>CATP</b> (ATM Card Transactions)</summary>

* catp.001.001.03
* catp.002.001.03
* catp.003.001.03
* catp.004.001.03
* catp.005.001.02
* catp.006.001.03
* catp.007.001.03
* catp.008.001.03
* catp.009.001.03
* catp.010.001.03
* catp.011.001.03
* catp.012.001.02
* catp.013.001.02
* catp.014.001.02
* catp.015.001.02
* catp.016.001.02
* catp.017.001.02

</details>

<details>
<summary><b>COLR</b> (Collateral Management)</summary>

* colr.001.001.02
* colr.002.001.02
* colr.003.001.05
* colr.004.001.05
* colr.005.001.06
* colr.006.001.05
* colr.007.001.06
* colr.008.001.06
* colr.009.001.05
* colr.010.001.05
* colr.011.001.05
* colr.012.001.05
* colr.013.001.05
* colr.014.001.05
* colr.015.001.05
* colr.016.001.05
* colr.019.001.01
* colr.020.001.01
* colr.021.001.01
* colr.022.001.01
* colr.023.001.01
* colr.024.001.01
* reda.074.001.01

</details>

<details>
<summary><b>FXTR</b> (Foreign Exchange Trade)</summary>

* fxtr.008.001.08
* fxtr.013.001.03
* fxtr.014.001.06
* fxtr.015.001.06
* fxtr.016.001.06
* fxtr.017.001.06
* fxtr.030.001.06
* fxtr.031.001.02
* fxtr.032.001.02
* fxtr.033.001.02
* fxtr.034.001.02
* fxtr.035.001.02
* fxtr.036.001.02
* fxtr.037.001.02
* fxtr.038.001.02

</details>

<details>
<summary><b>HEAD</b> (Business Application Header)</summary>

* head.001.001.02
* head.001.001.04
* head.002.001.01

</details>

<details>
<summary><b>PACS</b> (Payments Clearing and Settlement)</summary>

* pacs.002.001.12
* pacs.002.001.15
* pacs.003.001.11
* pacs.004.001.14
* pacs.007.001.13
* pacs.008.001.13
* pacs.009.001.12
* pacs.010.001.06
* pacs.028.001.06
* pacs.029.001.02

</details>

<details>
<summary><b>PAIN</b> (Payments Initiation)</summary>

* pain.001.001.12
* pain.002.001.14
* pain.007.001.12
* pain.008.001.11
* pain.009.001.08
* pain.010.001.08
* pain.011.001.08
* pain.012.001.08
* pain.013.001.11
* pain.014.001.11
* pain.017.001.04
* pain.018.001.04

</details>

<details>
<summary><b>REDA</b> (Reference Data)</summary>

* reda.001.001.04
* reda.002.001.04
* reda.004.001.07
* reda.005.001.03
* reda.006.001.01
* reda.007.001.01
* reda.008.001.01
* reda.009.001.01
* reda.010.001.01
* reda.012.001.01
* reda.013.001.01
* reda.014.001.02
* reda.015.001.01
* reda.016.001.01
* reda.017.001.02
* reda.018.001.01
* reda.019.001.01
* reda.020.001.01
* reda.021.001.01
* reda.022.001.02
* reda.023.001.01
* reda.029.001.01
* reda.030.001.01
* reda.031.001.01
* reda.032.001.01
* reda.033.001.01
* reda.034.001.01
* reda.035.001.01
* reda.036.001.01
* reda.037.001.01
* reda.041.001.02
* reda.042.001.01
* reda.043.001.02
* reda.045.001.01
* reda.046.001.01
* reda.047.001.01
* reda.049.001.01
* reda.050.001.01
* reda.051.001.01
* reda.056.001.01
* reda.057.001.01
* reda.058.001.01
* reda.059.001.01
* reda.060.001.02
* reda.061.001.02
* reda.064.001.02
* reda.065.001.02
* reda.066.001.02
* reda.067.001.02
* reda.068.001.02
* reda.069.001.02
* reda.070.001.02
* reda.071.001.02
* reda.072.001.02
* reda.073.001.02

</details>

<details>
<summary><b>REMT</b> (Payments Remittance Advice)</summary>

* remt.001.001.06
* remt.002.001.03

</details>

<details>
<summary><b>SECL</b> (Securities Clearing)</summary>

* secl.001.001.04
* secl.002.001.04
* secl.003.001.04
* secl.004.001.04
* secl.005.001.02
* secl.006.001.02
* secl.007.001.03
* secl.008.001.03
* secl.009.001.03
* secl.010.001.04

</details>

<details>
<summary><b>SEEV</b> (Securities Events)</summary>

* seev.001.001.12
* seev.002.001.10
* seev.003.001.10
* seev.004.001.10
* seev.005.001.10
* seev.006.001.11
* seev.007.001.11
* seev.008.001.10
* seev.009.001.02
* seev.010.001.01
* seev.011.001.03
* seev.012.001.01
* seev.013.001.01
* seev.014.001.01
* seev.015.001.01
* seev.016.001.01
* seev.017.001.01
* seev.018.001.01
* seev.019.001.01
* seev.020.001.01
* seev.021.001.01
* seev.022.001.01
* seev.023.001.01
* seev.024.001.01
* seev.025.001.01
* seev.026.001.01
* seev.027.001.01
* seev.028.001.01
* seev.029.001.01
* seev.030.001.01
* seev.031.001.15
* seev.031.002.15
* seev.032.001.09
* seev.032.002.09
* seev.033.001.13
* seev.033.002.13
* seev.034.001.15
* seev.034.002.15
* seev.035.001.16
* seev.035.002.16
* seev.036.001.16
* seev.036.002.16
* seev.037.001.16
* seev.037.002.16
* seev.038.001.09
* seev.038.002.09
* seev.039.001.13
* seev.039.002.13
* seev.040.001.13
* seev.040.002.13
* seev.041.001.14
* seev.041.002.14
* seev.042.001.13
* seev.042.002.13
* seev.044.001.13
* seev.044.002.13
* seev.045.001.04
* seev.046.001.01
* seev.047.001.03
* seev.048.001.01
* seev.049.001.01
* seev.050.001.03
* seev.051.001.02
* seev.052.001.03
* seev.053.001.03

</details>

<details>
<summary><b>SEMT</b> (Securities Management)</summary>

* semt.001.001.03
* semt.001.001.04
* semt.002.001.02
* semt.002.001.12
* semt.002.002.11
* semt.003.001.02
* semt.003.001.12
* semt.003.002.11
* semt.004.001.02
* semt.005.001.02
* semt.006.001.03
* semt.007.001.03
* semt.013.001.07
* semt.013.002.06
* semt.014.001.08
* semt.014.002.07
* semt.015.001.10
* semt.015.002.09
* semt.016.001.10
* semt.016.002.09
* semt.017.001.13
* semt.017.002.12
* semt.018.001.14
* semt.018.002.13
* semt.019.001.11
* semt.019.002.10
* semt.020.001.07
* semt.020.002.07
* semt.021.001.08
* semt.021.002.08
* semt.022.001.06
* semt.022.002.05
* semt.023.001.02
* semt.024.001.01
* semt.041.001.02
* semt.042.001.01

</details>

<details>
<summary><b>SESE</b> (Securities Settlement)</summary>

* sese.001.001.09
* sese.002.001.09
* sese.003.001.09
* sese.004.001.09
* sese.005.001.09
* sese.006.001.09
* sese.007.001.09
* sese.008.001.09
* sese.009.001.08
* sese.010.001.07
* sese.011.001.09
* sese.012.001.11
* sese.013.001.11
* sese.014.001.09
* sese.018.001.09
* sese.019.001.08
* sese.020.001.08
* sese.020.002.07
* sese.021.001.07
* sese.021.002.06
* sese.022.001.07
* sese.022.002.06
* sese.023.001.12
* sese.023.002.11
* sese.024.001.13
* sese.024.002.12
* sese.025.001.12
* sese.025.002.11
* sese.026.001.11
* sese.026.002.10
* sese.027.001.08
* sese.027.002.07
* sese.028.001.11
* sese.028.002.10
* sese.029.001.07
* sese.029.002.06
* sese.030.001.10
* sese.030.002.09
* sese.031.001.10
* sese.031.002.09
* sese.032.001.12
* sese.032.002.11
* sese.033.001.12
* sese.033.002.11
* sese.034.001.10
* sese.034.002.09
* sese.035.001.12
* sese.035.002.11
* sese.036.001.09
* sese.036.002.08
* sese.037.001.08
* sese.037.002.07
* sese.038.001.10
* sese.038.002.09
* sese.039.001.07
* sese.039.002.06
* sese.040.001.05
* sese.040.002.04
* sese.041.001.02
* sese.042.001.02

</details>

<details>
<summary><b>SETR</b> (Securities Trade)</summary>

* sese.043.001.01
* setr.001.001.04
* setr.002.001.04
* setr.003.001.04
* setr.004.001.04
* setr.005.001.04
* setr.006.001.05
* setr.007.001.04
* setr.008.001.04
* setr.009.001.04
* setr.010.001.04
* setr.011.001.04
* setr.012.001.05
* setr.013.001.04
* setr.014.001.04
* setr.015.001.04
* setr.016.001.04
* setr.017.001.04
* setr.018.001.04
* setr.027.001.05
* setr.029.001.02
* setr.030.001.03
* setr.044.001.04
* setr.047.001.02
* setr.049.001.02
* setr.051.001.02
* setr.053.001.02
* setr.055.001.02
* setr.057.001.02
* setr.058.001.02

</details>

<details>
<summary><b>TRCK</b> (Payment Tracker)</summary>

* trck.001.001.04
* trck.002.001.03
* trck.004.001.03

</details>

<details>
<summary><b>TSIN</b> (Trade Services Initiation)</summary>

* tsin.001.001.01
* tsin.002.001.01
* tsin.003.001.01
* tsin.005.001.01
* tsin.006.001.01
* tsin.007.001.01
* tsin.008.001.01
* tsin.009.001.01
* tsin.010.001.01
* tsin.011.001.01
* tsin.012.001.01
* tsin.013.001.01

</details>

<details>
<summary><b>TSMT</b> (Trade Services Management)</summary>

* tsmt.001.001.03
* tsmt.002.001.04
* tsmt.003.001.03
* tsmt.004.001.02
* tsmt.005.001.02
* tsmt.006.001.03
* tsmt.007.001.02
* tsmt.008.001.03
* tsmt.009.001.05
* tsmt.010.001.03
* tsmt.011.001.04
* tsmt.012.001.05
* tsmt.013.001.03
* tsmt.014.001.05
* tsmt.015.001.03
* tsmt.016.001.03
* tsmt.017.001.05
* tsmt.018.001.05
* tsmt.019.001.05
* tsmt.020.001.02
* tsmt.021.001.03
* tsmt.022.001.02
* tsmt.023.001.03
* tsmt.024.001.03
* tsmt.025.001.03
* tsmt.026.001.02
* tsmt.027.001.02
* tsmt.028.001.03
* tsmt.029.001.02
* tsmt.030.001.03
* tsmt.031.001.03
* tsmt.032.001.03
* tsmt.033.001.03
* tsmt.034.001.03
* tsmt.035.001.03
* tsmt.036.001.03
* tsmt.038.001.03
* tsmt.040.001.03
* tsmt.041.001.03
* tsmt.042.001.03
* tsmt.044.001.02
* tsmt.045.001.02
* tsmt.046.001.01
* tsmt.047.001.01
* tsmt.048.001.01
* tsmt.049.001.01
* tsmt.050.001.01
* tsmt.051.001.01
* tsmt.052.001.01
* tsmt.053.001.01
* tsmt.054.001.01
* tsmt.055.001.01

</details>

<details>
<summary><b>TSRV</b> (Trade Services)</summary>

* tsrv.001.001.01
* tsrv.002.001.01
* tsrv.003.001.01
* tsrv.004.001.01
* tsrv.005.001.01
* tsrv.006.001.01
* tsrv.007.001.01
* tsrv.008.001.01
* tsrv.009.001.01
* tsrv.010.001.01
* tsrv.011.001.01
* tsrv.012.001.01
* tsrv.013.001.01
* tsrv.014.001.01
* tsrv.015.001.01
* tsrv.016.001.01
* tsrv.017.001.01
* tsrv.018.001.01
* tsrv.019.001.01

</details>