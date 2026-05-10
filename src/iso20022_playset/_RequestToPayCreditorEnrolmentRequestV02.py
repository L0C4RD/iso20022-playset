from . import base_types
from ._CreditorEnrolment5 import CreditorEnrolment5
from ._SupplementaryData1 import SupplementaryData1
from ._CreditorInvoice6 import CreditorInvoice6
from ._EnrolmentHeader3 import EnrolmentHeader3

class RequestToPayCreditorEnrolmentRequestV02(base_types._BaseFieldType):

	__slots__ = ["_CdtrEnrlmnt", "_SplmtryData", "_Hdr", "_ActvtnData"]
	@property
	def CdtrEnrlmnt(self):
		return self._CdtrEnrlmnt

	@CdtrEnrlmnt.setter
	def CdtrEnrlmnt(self, value):
		self._CdtrEnrlmnt = value if type(value) != base_types.auto else self.make_default("CdtrEnrlmnt")

	@CdtrEnrlmnt.deleter
	def CdtrEnrlmnt(self):
		del self._CdtrEnrlmnt
		self._CdtrEnrlmnt = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def ActvtnData(self):
		return self._ActvtnData

	@ActvtnData.setter
	def ActvtnData(self, value):
		self._ActvtnData = value if type(value) != base_types.auto else self.make_default("ActvtnData")

	@ActvtnData.deleter
	def ActvtnData(self):
		del self._ActvtnData
		self._ActvtnData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtrEnrlmnt', type=CreditorEnrolment5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Hdr', type=EnrolmentHeader3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtnData', type=CreditorInvoice6, min=1, max=1, mutex_group=None, array=False),
	))

