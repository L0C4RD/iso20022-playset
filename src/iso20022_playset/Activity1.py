from . import base_types
import Max140Text
import Max70Text

class Activity1(base_types._BaseFieldType):

	__slots__ = ["_MsgNm", "_Desc"]
	@property
	def MsgNm(self):
		return self._MsgNm

	@MsgNm.setter
	def MsgNm(self, value):
		self._MsgNm = value if type(value) != auto else self.make_default("MsgNm")

	@MsgNm.deleter
	def MsgNm(self):
		del self._MsgNm
		self._MsgNm = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNm', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

