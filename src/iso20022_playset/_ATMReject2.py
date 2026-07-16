# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommand7
from . import Max100KBinary
from . import Max35Text
from . import Max500Text
from . import RejectReason1Code

class ATMReject2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Cmd", "_MsgInErr", "_RjctInitrId", "_RjctRsn"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max500Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max500Text, False)

	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if value is not None else base_types.UninitialisedField(self, 'Cmd', ATMCommand7, True)

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = base_types.UninitialisedField(self, 'Cmd', ATMCommand7, True)

	@property
	def MsgInErr(self):
		return self._MsgInErr

	@MsgInErr.setter
	def MsgInErr(self, value):
		self._MsgInErr = value if value is not None else base_types.UninitialisedField(self, 'MsgInErr', Max100KBinary, False)

	@MsgInErr.deleter
	def MsgInErr(self):
		del self._MsgInErr
		self._MsgInErr = base_types.UninitialisedField(self, 'MsgInErr', Max100KBinary, False)

	@property
	def RjctInitrId(self):
		return self._RjctInitrId

	@RjctInitrId.setter
	def RjctInitrId(self, value):
		self._RjctInitrId = value if value is not None else base_types.UninitialisedField(self, 'RjctInitrId', Max35Text, False)

	@RjctInitrId.deleter
	def RjctInitrId(self):
		del self._RjctInitrId
		self._RjctInitrId = base_types.UninitialisedField(self, 'RjctInitrId', Max35Text, False)

	@property
	def RjctRsn(self):
		return self._RjctRsn

	@RjctRsn.setter
	def RjctRsn(self, value):
		self._RjctRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctRsn', RejectReason1Code, False)

	@RjctRsn.deleter
	def RjctRsn(self):
		del self._RjctRsn
		self._RjctRsn = base_types.UninitialisedField(self, 'RjctRsn', RejectReason1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgInErr', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctInitrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctRsn', type=RejectReason1Code, min=1, max=1, mutex_group=None, array=False),
	))