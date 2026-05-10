import base_types
import CurrencyControlHeader8
import SupplementaryData1
import RegisteredContract16

class ContractRegistrationAmendmentRequestV04(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_SplmtryData", "_CtrctRegnAmdmnt"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def CtrctRegnAmdmnt(self):
		return self._CtrctRegnAmdmnt

	@CtrctRegnAmdmnt.setter
	def CtrctRegnAmdmnt(self, value):
		self._CtrctRegnAmdmnt = value if type(value) != auto else self.make_default("CtrctRegnAmdmnt")

	@CtrctRegnAmdmnt.deleter
	def CtrctRegnAmdmnt(self):
		del self._CtrctRegnAmdmnt
		self._CtrctRegnAmdmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=CurrencyControlHeader8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctRegnAmdmnt', type=RegisteredContract16, min=1, max=None, mutex_group=None, array=True),
	))

