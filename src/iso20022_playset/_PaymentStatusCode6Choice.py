from . import base_types
from ._FinalStatus1Code import FinalStatus1Code
from ._Max35Text import Max35Text
from ._Max4AlphaNumericText import Max4AlphaNumericText
from ._PendingStatus4Code import PendingStatus4Code

class PaymentStatusCode6Choice(base_types._BaseFieldType):

	__slots__ = ["_Fnl", "_Pdg", "_Prtry", "_RTGS", "_Sttlm"]
	@property
	def Fnl(self):
		return self._Fnl

	@Fnl.setter
	def Fnl(self, value):
		self._Fnl = value if type(value) != base_types.auto else self.make_default("Fnl")

	@Fnl.deleter
	def Fnl(self):
		del self._Fnl
		self._Fnl = None

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if type(value) != base_types.auto else self.make_default("Pdg")

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def RTGS(self):
		return self._RTGS

	@RTGS.setter
	def RTGS(self, value):
		self._RTGS = value if type(value) != base_types.auto else self.make_default("RTGS")

	@RTGS.deleter
	def RTGS(self):
		del self._RTGS
		self._RTGS = None

	@property
	def Sttlm(self):
		return self._Sttlm

	@Sttlm.setter
	def Sttlm(self, value):
		self._Sttlm = value if type(value) != base_types.auto else self.make_default("Sttlm")

	@Sttlm.deleter
	def Sttlm(self):
		del self._Sttlm
		self._Sttlm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fnl', type=FinalStatus1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus4Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RTGS', type=Max4AlphaNumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sttlm', type=Max4AlphaNumericText, min=0, max=1, mutex_group=1, array=False),
	))

