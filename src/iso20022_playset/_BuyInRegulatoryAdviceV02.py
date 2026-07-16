# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyInAdviceDetails2
from . import PartyIdentification144
from . import SecuritiesAccount19
from . import SupplementaryData1

class BuyInRegulatoryAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_BuyInAttrbts", "_SfkpgAcct", "_SplmtryData"]
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
		base_types.FieldEntry(name='BuyInAttrbts', type=BuyInAdviceDetails2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))