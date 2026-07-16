# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDevice1Code
from . import Max20000Text
from . import Max35Binary
from . import Max35Text
from . import OutputFormat2Code

class ActionMessage4(base_types._BaseFieldType):

	__slots__ = ["_Dvc", "_Frmt", "_Msg", "_MsgCnttSgntr", "_Ref"]
	@property
	def Dvc(self):
		return self._Dvc

	@Dvc.setter
	def Dvc(self, value):
		self._Dvc = value if value is not None else base_types.UninitialisedField(self, 'Dvc', ATMDevice1Code, False)

	@Dvc.deleter
	def Dvc(self):
		del self._Dvc
		self._Dvc = base_types.UninitialisedField(self, 'Dvc', ATMDevice1Code, False)

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if value is not None else base_types.UninitialisedField(self, 'Frmt', OutputFormat2Code, False)

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = base_types.UninitialisedField(self, 'Frmt', OutputFormat2Code, False)

	@property
	def Msg(self):
		return self._Msg

	@Msg.setter
	def Msg(self, value):
		self._Msg = value if value is not None else base_types.UninitialisedField(self, 'Msg', Max20000Text, False)

	@Msg.deleter
	def Msg(self):
		del self._Msg
		self._Msg = base_types.UninitialisedField(self, 'Msg', Max20000Text, False)

	@property
	def MsgCnttSgntr(self):
		return self._MsgCnttSgntr

	@MsgCnttSgntr.setter
	def MsgCnttSgntr(self, value):
		self._MsgCnttSgntr = value if value is not None else base_types.UninitialisedField(self, 'MsgCnttSgntr', Max35Binary, False)

	@MsgCnttSgntr.deleter
	def MsgCnttSgntr(self):
		del self._MsgCnttSgntr
		self._MsgCnttSgntr = base_types.UninitialisedField(self, 'MsgCnttSgntr', Max35Binary, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dvc', type=ATMDevice1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=OutputFormat2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Msg', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgCnttSgntr', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))