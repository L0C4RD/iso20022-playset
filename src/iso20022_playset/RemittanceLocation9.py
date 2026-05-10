from . import base_types
import NameAndAddress18
import Max2048Text
import Max35Text
import RemittanceLocationMethod2Code

class RemittanceLocation9(base_types._BaseFieldType):

	__slots__ = ["_RmtId", "_RmtLctnPstlAdr", "_RmtLctnElctrncAdr", "_RmtLctnMtd"]
	@property
	def RmtId(self):
		return self._RmtId

	@RmtId.setter
	def RmtId(self, value):
		self._RmtId = value if type(value) != auto else self.make_default("RmtId")

	@RmtId.deleter
	def RmtId(self):
		del self._RmtId
		self._RmtId = None

	@property
	def RmtLctnPstlAdr(self):
		return self._RmtLctnPstlAdr

	@RmtLctnPstlAdr.setter
	def RmtLctnPstlAdr(self, value):
		self._RmtLctnPstlAdr = value if type(value) != auto else self.make_default("RmtLctnPstlAdr")

	@RmtLctnPstlAdr.deleter
	def RmtLctnPstlAdr(self):
		del self._RmtLctnPstlAdr
		self._RmtLctnPstlAdr = None

	@property
	def RmtLctnElctrncAdr(self):
		return self._RmtLctnElctrncAdr

	@RmtLctnElctrncAdr.setter
	def RmtLctnElctrncAdr(self, value):
		self._RmtLctnElctrncAdr = value if type(value) != auto else self.make_default("RmtLctnElctrncAdr")

	@RmtLctnElctrncAdr.deleter
	def RmtLctnElctrncAdr(self):
		del self._RmtLctnElctrncAdr
		self._RmtLctnElctrncAdr = None

	@property
	def RmtLctnMtd(self):
		return self._RmtLctnMtd

	@RmtLctnMtd.setter
	def RmtLctnMtd(self, value):
		self._RmtLctnMtd = value if type(value) != auto else self.make_default("RmtLctnMtd")

	@RmtLctnMtd.deleter
	def RmtLctnMtd(self):
		del self._RmtLctnMtd
		self._RmtLctnMtd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtLctnPstlAdr', type=NameAndAddress18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtLctnElctrncAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtLctnMtd', type=RemittanceLocationMethod2Code, min=0, max=1, mutex_group=None, array=False),
	))

