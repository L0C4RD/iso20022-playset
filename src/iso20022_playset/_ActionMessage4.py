from . import base_types
from ._Max20000Text import Max20000Text
from ._OutputFormat2Code import OutputFormat2Code
from ._Max35Text import Max35Text
from ._Max35Binary import Max35Binary
from ._ATMDevice1Code import ATMDevice1Code

class ActionMessage4(base_types._BaseFieldType):

	__slots__ = ["_Msg", "_Ref", "_Frmt", "_MsgCnttSgntr", "_Dvc"]
	@property
	def Dvc(self):
		return self._Dvc

	@Dvc.setter
	def Dvc(self, value):
		self._Dvc = value if type(value) != base_types.auto else self.make_default("Dvc")

	@Dvc.deleter
	def Dvc(self):
		del self._Dvc
		self._Dvc = None

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if type(value) != base_types.auto else self.make_default("Frmt")

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = None

	@property
	def Msg(self):
		return self._Msg

	@Msg.setter
	def Msg(self, value):
		self._Msg = value if type(value) != base_types.auto else self.make_default("Msg")

	@Msg.deleter
	def Msg(self):
		del self._Msg
		self._Msg = None

	@property
	def MsgCnttSgntr(self):
		return self._MsgCnttSgntr

	@MsgCnttSgntr.setter
	def MsgCnttSgntr(self, value):
		self._MsgCnttSgntr = value if type(value) != base_types.auto else self.make_default("MsgCnttSgntr")

	@MsgCnttSgntr.deleter
	def MsgCnttSgntr(self):
		del self._MsgCnttSgntr
		self._MsgCnttSgntr = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dvc', type=ATMDevice1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=OutputFormat2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Msg', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgCnttSgntr', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

