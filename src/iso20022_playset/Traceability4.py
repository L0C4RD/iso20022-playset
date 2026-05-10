import base_types
import Max35Text
import ISODateTime
import GenericIdentification77

class Traceability4(base_types._BaseFieldType):

	__slots__ = ["_TracDtTmIn", "_RlayId", "_TracDtTmOut", "_SeqNb"]
	@property
	def TracDtTmIn(self):
		return self._TracDtTmIn

	@TracDtTmIn.setter
	def TracDtTmIn(self, value):
		self._TracDtTmIn = value if type(value) != auto else self.make_default("TracDtTmIn")

	@TracDtTmIn.deleter
	def TracDtTmIn(self):
		del self._TracDtTmIn
		self._TracDtTmIn = None

	@property
	def RlayId(self):
		return self._RlayId

	@RlayId.setter
	def RlayId(self, value):
		self._RlayId = value if type(value) != auto else self.make_default("RlayId")

	@RlayId.deleter
	def RlayId(self):
		del self._RlayId
		self._RlayId = None

	@property
	def TracDtTmOut(self):
		return self._TracDtTmOut

	@TracDtTmOut.setter
	def TracDtTmOut(self, value):
		self._TracDtTmOut = value if type(value) != auto else self.make_default("TracDtTmOut")

	@TracDtTmOut.deleter
	def TracDtTmOut(self):
		del self._TracDtTmOut
		self._TracDtTmOut = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TracDtTmIn', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RlayId', type=GenericIdentification77, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TracDtTmOut', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

