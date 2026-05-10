from . import base_types
from ._PartyIdentification43 import PartyIdentification43
from ._ExpiryDetails1 import ExpiryDetails1
from ._Narrative1 import Narrative1
from ._CommunicationChannel1 import CommunicationChannel1
from ._UndertakingAmount2 import UndertakingAmount2

class Undertaking11(base_types._BaseFieldType):

	__slots__ = ["_NewUdrtkgTermsAndConds", "_NewXpryDtls", "_NewBnfcry", "_DlvryChanl", "_NewUdrtkgAmt"]
	@property
	def DlvryChanl(self):
		return self._DlvryChanl

	@DlvryChanl.setter
	def DlvryChanl(self, value):
		self._DlvryChanl = value if type(value) != base_types.auto else self.make_default("DlvryChanl")

	@DlvryChanl.deleter
	def DlvryChanl(self):
		del self._DlvryChanl
		self._DlvryChanl = None

	@property
	def NewBnfcry(self):
		return self._NewBnfcry

	@NewBnfcry.setter
	def NewBnfcry(self, value):
		self._NewBnfcry = value if type(value) != base_types.auto else self.make_default("NewBnfcry")

	@NewBnfcry.deleter
	def NewBnfcry(self):
		del self._NewBnfcry
		self._NewBnfcry = None

	@property
	def NewUdrtkgAmt(self):
		return self._NewUdrtkgAmt

	@NewUdrtkgAmt.setter
	def NewUdrtkgAmt(self, value):
		self._NewUdrtkgAmt = value if type(value) != base_types.auto else self.make_default("NewUdrtkgAmt")

	@NewUdrtkgAmt.deleter
	def NewUdrtkgAmt(self):
		del self._NewUdrtkgAmt
		self._NewUdrtkgAmt = None

	@property
	def NewUdrtkgTermsAndConds(self):
		return self._NewUdrtkgTermsAndConds

	@NewUdrtkgTermsAndConds.setter
	def NewUdrtkgTermsAndConds(self, value):
		self._NewUdrtkgTermsAndConds = value if type(value) != base_types.auto else self.make_default("NewUdrtkgTermsAndConds")

	@NewUdrtkgTermsAndConds.deleter
	def NewUdrtkgTermsAndConds(self):
		del self._NewUdrtkgTermsAndConds
		self._NewUdrtkgTermsAndConds = None

	@property
	def NewXpryDtls(self):
		return self._NewXpryDtls

	@NewXpryDtls.setter
	def NewXpryDtls(self, value):
		self._NewXpryDtls = value if type(value) != base_types.auto else self.make_default("NewXpryDtls")

	@NewXpryDtls.deleter
	def NewXpryDtls(self):
		del self._NewXpryDtls
		self._NewXpryDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvryChanl', type=CommunicationChannel1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewBnfcry', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewUdrtkgAmt', type=UndertakingAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewUdrtkgTermsAndConds', type=Narrative1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewXpryDtls', type=ExpiryDetails1, min=0, max=1, mutex_group=None, array=False),
	))

