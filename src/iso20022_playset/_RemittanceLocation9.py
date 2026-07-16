# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2048Text
from . import Max35Text
from . import NameAndAddress18
from . import RemittanceLocationMethod2Code

class RemittanceLocation9(base_types._BaseFieldType):

	__slots__ = ["_RmtId", "_RmtLctnElctrncAdr", "_RmtLctnMtd", "_RmtLctnPstlAdr"]
	@property
	def RmtId(self):
		return self._RmtId

	@RmtId.setter
	def RmtId(self, value):
		self._RmtId = value if value is not None else base_types.UninitialisedField(self, 'RmtId', Max35Text, False)

	@RmtId.deleter
	def RmtId(self):
		del self._RmtId
		self._RmtId = base_types.UninitialisedField(self, 'RmtId', Max35Text, False)

	@property
	def RmtLctnElctrncAdr(self):
		return self._RmtLctnElctrncAdr

	@RmtLctnElctrncAdr.setter
	def RmtLctnElctrncAdr(self, value):
		self._RmtLctnElctrncAdr = value if value is not None else base_types.UninitialisedField(self, 'RmtLctnElctrncAdr', Max2048Text, False)

	@RmtLctnElctrncAdr.deleter
	def RmtLctnElctrncAdr(self):
		del self._RmtLctnElctrncAdr
		self._RmtLctnElctrncAdr = base_types.UninitialisedField(self, 'RmtLctnElctrncAdr', Max2048Text, False)

	@property
	def RmtLctnMtd(self):
		return self._RmtLctnMtd

	@RmtLctnMtd.setter
	def RmtLctnMtd(self, value):
		self._RmtLctnMtd = value if value is not None else base_types.UninitialisedField(self, 'RmtLctnMtd', RemittanceLocationMethod2Code, False)

	@RmtLctnMtd.deleter
	def RmtLctnMtd(self):
		del self._RmtLctnMtd
		self._RmtLctnMtd = base_types.UninitialisedField(self, 'RmtLctnMtd', RemittanceLocationMethod2Code, False)

	@property
	def RmtLctnPstlAdr(self):
		return self._RmtLctnPstlAdr

	@RmtLctnPstlAdr.setter
	def RmtLctnPstlAdr(self, value):
		self._RmtLctnPstlAdr = value if value is not None else base_types.UninitialisedField(self, 'RmtLctnPstlAdr', NameAndAddress18, False)

	@RmtLctnPstlAdr.deleter
	def RmtLctnPstlAdr(self):
		del self._RmtLctnPstlAdr
		self._RmtLctnPstlAdr = base_types.UninitialisedField(self, 'RmtLctnPstlAdr', NameAndAddress18, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtLctnElctrncAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtLctnMtd', type=RemittanceLocationMethod2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtLctnPstlAdr', type=NameAndAddress18, min=0, max=1, mutex_group=None, array=False),
	))