# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateSectorCriteria5
from . import PartyNatureType1Code
from . import SecuritiesTradeVenueCriteria1Choice
from . import TransactionOperationType6Code

class TradeAdditionalQueryCriteria7(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_CorpSctr", "_ExctnVn", "_NtrOfCtrPty"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', TransactionOperationType6Code, True)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', TransactionOperationType6Code, True)

	@property
	def CorpSctr(self):
		return self._CorpSctr

	@CorpSctr.setter
	def CorpSctr(self, value):
		self._CorpSctr = value if value is not None else base_types.UninitialisedField(self, 'CorpSctr', CorporateSectorCriteria5, True)

	@CorpSctr.deleter
	def CorpSctr(self):
		del self._CorpSctr
		self._CorpSctr = base_types.UninitialisedField(self, 'CorpSctr', CorporateSectorCriteria5, True)

	@property
	def ExctnVn(self):
		return self._ExctnVn

	@ExctnVn.setter
	def ExctnVn(self, value):
		self._ExctnVn = value if value is not None else base_types.UninitialisedField(self, 'ExctnVn', SecuritiesTradeVenueCriteria1Choice, False)

	@ExctnVn.deleter
	def ExctnVn(self):
		del self._ExctnVn
		self._ExctnVn = base_types.UninitialisedField(self, 'ExctnVn', SecuritiesTradeVenueCriteria1Choice, False)

	@property
	def NtrOfCtrPty(self):
		return self._NtrOfCtrPty

	@NtrOfCtrPty.setter
	def NtrOfCtrPty(self, value):
		self._NtrOfCtrPty = value if value is not None else base_types.UninitialisedField(self, 'NtrOfCtrPty', PartyNatureType1Code, True)

	@NtrOfCtrPty.deleter
	def NtrOfCtrPty(self):
		del self._NtrOfCtrPty
		self._NtrOfCtrPty = base_types.UninitialisedField(self, 'NtrOfCtrPty', PartyNatureType1Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TransactionOperationType6Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpSctr', type=CorporateSectorCriteria5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ExctnVn', type=SecuritiesTradeVenueCriteria1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtrOfCtrPty', type=PartyNatureType1Code, min=0, max=None, mutex_group=None, array=True),
	))