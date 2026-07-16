# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification49
from . import PartyIdentification99Choice
from . import SettlementParties32

class SettlementParties35(base_types._BaseFieldType):

	__slots__ = ["_LclMktId", "_RegnDtls", "_StgSttlmPties"]
	@property
	def LclMktId(self):
		return self._LclMktId

	@LclMktId.setter
	def LclMktId(self, value):
		self._LclMktId = value if value is not None else base_types.UninitialisedField(self, 'LclMktId', GenericIdentification49, True)

	@LclMktId.deleter
	def LclMktId(self):
		del self._LclMktId
		self._LclMktId = base_types.UninitialisedField(self, 'LclMktId', GenericIdentification49, True)

	@property
	def RegnDtls(self):
		return self._RegnDtls

	@RegnDtls.setter
	def RegnDtls(self, value):
		self._RegnDtls = value if value is not None else base_types.UninitialisedField(self, 'RegnDtls', PartyIdentification99Choice, False)

	@RegnDtls.deleter
	def RegnDtls(self):
		del self._RegnDtls
		self._RegnDtls = base_types.UninitialisedField(self, 'RegnDtls', PartyIdentification99Choice, False)

	@property
	def StgSttlmPties(self):
		return self._StgSttlmPties

	@StgSttlmPties.setter
	def StgSttlmPties(self, value):
		self._StgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'StgSttlmPties', SettlementParties32, False)

	@StgSttlmPties.deleter
	def StgSttlmPties(self):
		del self._StgSttlmPties
		self._StgSttlmPties = base_types.UninitialisedField(self, 'StgSttlmPties', SettlementParties32, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LclMktId', type=GenericIdentification49, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnDtls', type=PartyIdentification99Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgSttlmPties', type=SettlementParties32, min=1, max=1, mutex_group=None, array=False),
	))