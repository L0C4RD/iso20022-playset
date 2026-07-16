# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyControlHeader9
from . import SupplementaryData1
from . import SupportingDocument4

class CurrencyControlSupportingDocumentDeliveryV04(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_SplmtryData", "_SpprtgDoc"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', CurrencyControlHeader9, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', CurrencyControlHeader9, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def SpprtgDoc(self):
		return self._SpprtgDoc

	@SpprtgDoc.setter
	def SpprtgDoc(self, value):
		self._SpprtgDoc = value if value is not None else base_types.UninitialisedField(self, 'SpprtgDoc', SupportingDocument4, True)

	@SpprtgDoc.deleter
	def SpprtgDoc(self):
		del self._SpprtgDoc
		self._SpprtgDoc = base_types.UninitialisedField(self, 'SpprtgDoc', SupportingDocument4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=CurrencyControlHeader9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpprtgDoc', type=SupportingDocument4, min=1, max=None, mutex_group=None, array=True),
	))