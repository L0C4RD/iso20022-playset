import base_types
import CurrencyControlHeader9
import SupportingDocument4
import SupplementaryData1

class CurrencyControlSupportingDocumentDeliveryV04(base_types._BaseFieldType):

	__slots__ = ["_SpprtgDoc", "_SplmtryData", "_GrpHdr"]
	@property
	def SpprtgDoc(self):
		return self._SpprtgDoc

	@SpprtgDoc.setter
	def SpprtgDoc(self, value):
		self._SpprtgDoc = value if type(value) != auto else self.make_default("SpprtgDoc")

	@SpprtgDoc.deleter
	def SpprtgDoc(self):
		del self._SpprtgDoc
		self._SpprtgDoc = None

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
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SpprtgDoc', type=SupportingDocument4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=CurrencyControlHeader9, min=1, max=1, mutex_group=None, array=False),
	))

