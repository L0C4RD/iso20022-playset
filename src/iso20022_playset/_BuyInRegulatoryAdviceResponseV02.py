# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyInAdviceDetails2
from . import Identification14
from . import PartyIdentification144
from . import ProcessingStatus79Choice
from . import SecuritiesAccount19
from . import SupplementaryData1

class BuyInRegulatoryAdviceResponseV02(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AdvcRef", "_BuyInAttrbts", "_PrcgSts", "_SfkpgAcct", "_SplmtryData"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification144, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification144, False)

	@property
	def AdvcRef(self):
		return self._AdvcRef

	@AdvcRef.setter
	def AdvcRef(self, value):
		self._AdvcRef = value if value is not None else base_types.UninitialisedField(self, 'AdvcRef', Identification14, False)

	@AdvcRef.deleter
	def AdvcRef(self):
		del self._AdvcRef
		self._AdvcRef = base_types.UninitialisedField(self, 'AdvcRef', Identification14, False)

	@property
	def BuyInAttrbts(self):
		return self._BuyInAttrbts

	@BuyInAttrbts.setter
	def BuyInAttrbts(self, value):
		self._BuyInAttrbts = value if value is not None else base_types.UninitialisedField(self, 'BuyInAttrbts', BuyInAdviceDetails2, True)

	@BuyInAttrbts.deleter
	def BuyInAttrbts(self):
		del self._BuyInAttrbts
		self._BuyInAttrbts = base_types.UninitialisedField(self, 'BuyInAttrbts', BuyInAdviceDetails2, True)

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus79Choice, False)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus79Choice, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdvcRef', type=Identification14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInAttrbts', type=BuyInAdviceDetails2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus79Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))