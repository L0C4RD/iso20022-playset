from . import base_types
import Max350Text
import Status11Code
import Max35Text

class InstructionProcessingStatus6(base_types._BaseFieldType):

	__slots__ = ["_AttndncCardNb", "_Sts", "_AddtlInf"]
	@property
	def AttndncCardNb(self):
		return self._AttndncCardNb

	@AttndncCardNb.setter
	def AttndncCardNb(self, value):
		self._AttndncCardNb = value if type(value) != auto else self.make_default("AttndncCardNb")

	@AttndncCardNb.deleter
	def AttndncCardNb(self):
		del self._AttndncCardNb
		self._AttndncCardNb = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttndncCardNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=Status11Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

