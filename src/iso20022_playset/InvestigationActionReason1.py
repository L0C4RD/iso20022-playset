import base_types
import PartyIdentification135
import Max105Text
import InvestigationActionReason1Choice

class InvestigationActionReason1(base_types._BaseFieldType):

	__slots__ = ["_Orgtr", "_AddtlInf", "_Rsn"]
	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if type(value) != auto else self.make_default("Orgtr")

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Orgtr', type=PartyIdentification135, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max105Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rsn', type=InvestigationActionReason1Choice, min=1, max=1, mutex_group=None, array=False),
	))

