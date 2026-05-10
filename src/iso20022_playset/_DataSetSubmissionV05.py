from . import base_types
from ._BICIdentification1 import BICIdentification1
from ._CommercialDataSet5 import CommercialDataSet5
from ._CertificateDataSet2 import CertificateDataSet2
from ._MessageIdentification1 import MessageIdentification1
from ._DataSetSubmissionReferences3 import DataSetSubmissionReferences3
from ._TransportDataSet5 import TransportDataSet5
from ._OtherCertificateDataSet2 import OtherCertificateDataSet2
from ._SimpleIdentificationInformation import SimpleIdentificationInformation
from ._InsuranceDataSet1 import InsuranceDataSet1
from ._InstructionType3 import InstructionType3

class DataSetSubmissionV05(base_types._BaseFieldType):

	__slots__ = ["_BuyrBk", "_SellrBk", "_TrnsprtDataSet", "_CertDataSet", "_OthrCertDataSet", "_Instr", "_RltdTxRefs", "_CmonSubmissnRef", "_ComrclDataSet", "_InsrncDataSet", "_SubmissnId"]
	@property
	def BuyrBk(self):
		return self._BuyrBk

	@BuyrBk.setter
	def BuyrBk(self, value):
		self._BuyrBk = value if type(value) != base_types.auto else self.make_default("BuyrBk")

	@BuyrBk.deleter
	def BuyrBk(self):
		del self._BuyrBk
		self._BuyrBk = None

	@property
	def SellrBk(self):
		return self._SellrBk

	@SellrBk.setter
	def SellrBk(self, value):
		self._SellrBk = value if type(value) != base_types.auto else self.make_default("SellrBk")

	@SellrBk.deleter
	def SellrBk(self):
		del self._SellrBk
		self._SellrBk = None

	@property
	def TrnsprtDataSet(self):
		return self._TrnsprtDataSet

	@TrnsprtDataSet.setter
	def TrnsprtDataSet(self, value):
		self._TrnsprtDataSet = value if type(value) != base_types.auto else self.make_default("TrnsprtDataSet")

	@TrnsprtDataSet.deleter
	def TrnsprtDataSet(self):
		del self._TrnsprtDataSet
		self._TrnsprtDataSet = None

	@property
	def CertDataSet(self):
		return self._CertDataSet

	@CertDataSet.setter
	def CertDataSet(self, value):
		self._CertDataSet = value if type(value) != base_types.auto else self.make_default("CertDataSet")

	@CertDataSet.deleter
	def CertDataSet(self):
		del self._CertDataSet
		self._CertDataSet = None

	@property
	def OthrCertDataSet(self):
		return self._OthrCertDataSet

	@OthrCertDataSet.setter
	def OthrCertDataSet(self, value):
		self._OthrCertDataSet = value if type(value) != base_types.auto else self.make_default("OthrCertDataSet")

	@OthrCertDataSet.deleter
	def OthrCertDataSet(self):
		del self._OthrCertDataSet
		self._OthrCertDataSet = None

	@property
	def Instr(self):
		return self._Instr

	@Instr.setter
	def Instr(self, value):
		self._Instr = value if type(value) != base_types.auto else self.make_default("Instr")

	@Instr.deleter
	def Instr(self):
		del self._Instr
		self._Instr = None

	@property
	def RltdTxRefs(self):
		return self._RltdTxRefs

	@RltdTxRefs.setter
	def RltdTxRefs(self, value):
		self._RltdTxRefs = value if type(value) != base_types.auto else self.make_default("RltdTxRefs")

	@RltdTxRefs.deleter
	def RltdTxRefs(self):
		del self._RltdTxRefs
		self._RltdTxRefs = None

	@property
	def CmonSubmissnRef(self):
		return self._CmonSubmissnRef

	@CmonSubmissnRef.setter
	def CmonSubmissnRef(self, value):
		self._CmonSubmissnRef = value if type(value) != base_types.auto else self.make_default("CmonSubmissnRef")

	@CmonSubmissnRef.deleter
	def CmonSubmissnRef(self):
		del self._CmonSubmissnRef
		self._CmonSubmissnRef = None

	@property
	def ComrclDataSet(self):
		return self._ComrclDataSet

	@ComrclDataSet.setter
	def ComrclDataSet(self, value):
		self._ComrclDataSet = value if type(value) != base_types.auto else self.make_default("ComrclDataSet")

	@ComrclDataSet.deleter
	def ComrclDataSet(self):
		del self._ComrclDataSet
		self._ComrclDataSet = None

	@property
	def InsrncDataSet(self):
		return self._InsrncDataSet

	@InsrncDataSet.setter
	def InsrncDataSet(self, value):
		self._InsrncDataSet = value if type(value) != base_types.auto else self.make_default("InsrncDataSet")

	@InsrncDataSet.deleter
	def InsrncDataSet(self):
		del self._InsrncDataSet
		self._InsrncDataSet = None

	@property
	def SubmissnId(self):
		return self._SubmissnId

	@SubmissnId.setter
	def SubmissnId(self, value):
		self._SubmissnId = value if type(value) != base_types.auto else self.make_default("SubmissnId")

	@SubmissnId.deleter
	def SubmissnId(self):
		del self._SubmissnId
		self._SubmissnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtDataSet', type=TransportDataSet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertDataSet', type=CertificateDataSet2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrCertDataSet', type=OtherCertificateDataSet2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Instr', type=InstructionType3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdTxRefs', type=DataSetSubmissionReferences3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CmonSubmissnRef', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComrclDataSet', type=CommercialDataSet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncDataSet', type=InsuranceDataSet1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmissnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

