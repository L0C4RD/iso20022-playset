from . import base_types
from ._ProprietaryReason4 import ProprietaryReason4
from ._ProprietaryStatusAndReason6 import ProprietaryStatusAndReason6

class SettlementStatus27Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtlSttlm", "_Prtry", "_Sttld", "_Usttld"]
	@property
	def PrtlSttlm(self):
		return self._PrtlSttlm

	@PrtlSttlm.setter
	def PrtlSttlm(self, value):
		self._PrtlSttlm = value if type(value) != base_types.auto else self.make_default("PrtlSttlm")

	@PrtlSttlm.deleter
	def PrtlSttlm(self):
		del self._PrtlSttlm
		self._PrtlSttlm = None

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
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if type(value) != base_types.auto else self.make_default("Sttld")

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = None

	@property
	def Usttld(self):
		return self._Usttld

	@Usttld.setter
	def Usttld(self, value):
		self._Usttld = value if type(value) != base_types.auto else self.make_default("Usttld")

	@Usttld.deleter
	def Usttld(self):
		del self._Usttld
		self._Usttld = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtlSttlm', type=ProprietaryReason4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sttld', type=ProprietaryReason4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Usttld', type=ProprietaryReason4, min=1, max=None, mutex_group=1, array=True),
	))

