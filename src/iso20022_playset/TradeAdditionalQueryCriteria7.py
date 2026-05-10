import base_types
import SecuritiesTradeVenueCriteria1Choice
import CorporateSectorCriteria5
import TransactionOperationType6Code
import PartyNatureType1Code

class TradeAdditionalQueryCriteria7(base_types._BaseFieldType):

	__slots__ = ["_CorpSctr", "_NtrOfCtrPty", "_ExctnVn", "_ActnTp"]
	@property
	def CorpSctr(self):
		return self._CorpSctr

	@CorpSctr.setter
	def CorpSctr(self, value):
		self._CorpSctr = value if type(value) != auto else self.make_default("CorpSctr")

	@CorpSctr.deleter
	def CorpSctr(self):
		del self._CorpSctr
		self._CorpSctr = None

	@property
	def NtrOfCtrPty(self):
		return self._NtrOfCtrPty

	@NtrOfCtrPty.setter
	def NtrOfCtrPty(self, value):
		self._NtrOfCtrPty = value if type(value) != auto else self.make_default("NtrOfCtrPty")

	@NtrOfCtrPty.deleter
	def NtrOfCtrPty(self):
		del self._NtrOfCtrPty
		self._NtrOfCtrPty = None

	@property
	def ExctnVn(self):
		return self._ExctnVn

	@ExctnVn.setter
	def ExctnVn(self, value):
		self._ExctnVn = value if type(value) != auto else self.make_default("ExctnVn")

	@ExctnVn.deleter
	def ExctnVn(self):
		del self._ExctnVn
		self._ExctnVn = None

	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpSctr', type=CorporateSectorCriteria5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtrOfCtrPty', type=PartyNatureType1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ExctnVn', type=SecuritiesTradeVenueCriteria1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnTp', type=TransactionOperationType6Code, min=0, max=None, mutex_group=None, array=True),
	))

