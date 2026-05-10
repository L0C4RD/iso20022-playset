from . import base_types
from .PartyIdentification125Choice import PartyIdentification125Choice
from .Max140Text import Max140Text
from .CommunicationMethod3Choice import CommunicationMethod3Choice

class DocumentToSend4(base_types._BaseFieldType):

	__slots__ = ["_MtdOfTrnsmssn", "_Tp", "_Rcpt"]
	@property
	def MtdOfTrnsmssn(self):
		return self._MtdOfTrnsmssn

	@MtdOfTrnsmssn.setter
	def MtdOfTrnsmssn(self, value):
		self._MtdOfTrnsmssn = value if type(value) != base_types.auto else self.make_default("MtdOfTrnsmssn")

	@MtdOfTrnsmssn.deleter
	def MtdOfTrnsmssn(self):
		del self._MtdOfTrnsmssn
		self._MtdOfTrnsmssn = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if type(value) != base_types.auto else self.make_default("Rcpt")

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtdOfTrnsmssn', type=CommunicationMethod3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=PartyIdentification125Choice, min=1, max=1, mutex_group=None, array=False),
	))

