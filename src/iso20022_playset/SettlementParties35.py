import base_types
import GenericIdentification49
import PartyIdentification99Choice
import SettlementParties32

class SettlementParties35(base_types._BaseFieldType):

	__slots__ = ["_LclMktId", "_StgSttlmPties", "_RegnDtls"]
	@property
	def LclMktId(self):
		return self._LclMktId

	@LclMktId.setter
	def LclMktId(self, value):
		self._LclMktId = value if type(value) != auto else self.make_default("LclMktId")

	@LclMktId.deleter
	def LclMktId(self):
		del self._LclMktId
		self._LclMktId = None

	@property
	def StgSttlmPties(self):
		return self._StgSttlmPties

	@StgSttlmPties.setter
	def StgSttlmPties(self, value):
		self._StgSttlmPties = value if type(value) != auto else self.make_default("StgSttlmPties")

	@StgSttlmPties.deleter
	def StgSttlmPties(self):
		del self._StgSttlmPties
		self._StgSttlmPties = None

	@property
	def RegnDtls(self):
		return self._RegnDtls

	@RegnDtls.setter
	def RegnDtls(self, value):
		self._RegnDtls = value if type(value) != auto else self.make_default("RegnDtls")

	@RegnDtls.deleter
	def RegnDtls(self):
		del self._RegnDtls
		self._RegnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LclMktId', type=GenericIdentification49, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StgSttlmPties', type=SettlementParties32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDtls', type=PartyIdentification99Choice, min=0, max=1, mutex_group=None, array=False),
	))

