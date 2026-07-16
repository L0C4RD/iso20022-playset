# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationChannel1
from . import ExpiryDetails1
from . import Narrative1
from . import PartyIdentification43
from . import UndertakingAmount2

class Undertaking11(base_types._BaseFieldType):

	__slots__ = ["_DlvryChanl", "_NewBnfcry", "_NewUdrtkgAmt", "_NewUdrtkgTermsAndConds", "_NewXpryDtls"]
	@property
	def DlvryChanl(self):
		return self._DlvryChanl

	@DlvryChanl.setter
	def DlvryChanl(self, value):
		self._DlvryChanl = value if value is not None else base_types.UninitialisedField(self, 'DlvryChanl', CommunicationChannel1, False)

	@DlvryChanl.deleter
	def DlvryChanl(self):
		del self._DlvryChanl
		self._DlvryChanl = base_types.UninitialisedField(self, 'DlvryChanl', CommunicationChannel1, False)

	@property
	def NewBnfcry(self):
		return self._NewBnfcry

	@NewBnfcry.setter
	def NewBnfcry(self, value):
		self._NewBnfcry = value if value is not None else base_types.UninitialisedField(self, 'NewBnfcry', PartyIdentification43, False)

	@NewBnfcry.deleter
	def NewBnfcry(self):
		del self._NewBnfcry
		self._NewBnfcry = base_types.UninitialisedField(self, 'NewBnfcry', PartyIdentification43, False)

	@property
	def NewUdrtkgAmt(self):
		return self._NewUdrtkgAmt

	@NewUdrtkgAmt.setter
	def NewUdrtkgAmt(self, value):
		self._NewUdrtkgAmt = value if value is not None else base_types.UninitialisedField(self, 'NewUdrtkgAmt', UndertakingAmount2, False)

	@NewUdrtkgAmt.deleter
	def NewUdrtkgAmt(self):
		del self._NewUdrtkgAmt
		self._NewUdrtkgAmt = base_types.UninitialisedField(self, 'NewUdrtkgAmt', UndertakingAmount2, False)

	@property
	def NewUdrtkgTermsAndConds(self):
		return self._NewUdrtkgTermsAndConds

	@NewUdrtkgTermsAndConds.setter
	def NewUdrtkgTermsAndConds(self, value):
		self._NewUdrtkgTermsAndConds = value if value is not None else base_types.UninitialisedField(self, 'NewUdrtkgTermsAndConds', Narrative1, False)

	@NewUdrtkgTermsAndConds.deleter
	def NewUdrtkgTermsAndConds(self):
		del self._NewUdrtkgTermsAndConds
		self._NewUdrtkgTermsAndConds = base_types.UninitialisedField(self, 'NewUdrtkgTermsAndConds', Narrative1, False)

	@property
	def NewXpryDtls(self):
		return self._NewXpryDtls

	@NewXpryDtls.setter
	def NewXpryDtls(self, value):
		self._NewXpryDtls = value if value is not None else base_types.UninitialisedField(self, 'NewXpryDtls', ExpiryDetails1, False)

	@NewXpryDtls.deleter
	def NewXpryDtls(self):
		del self._NewXpryDtls
		self._NewXpryDtls = base_types.UninitialisedField(self, 'NewXpryDtls', ExpiryDetails1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvryChanl', type=CommunicationChannel1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewBnfcry', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewUdrtkgAmt', type=UndertakingAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewUdrtkgTermsAndConds', type=Narrative1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewXpryDtls', type=ExpiryDetails1, min=0, max=1, mutex_group=None, array=False),
	))