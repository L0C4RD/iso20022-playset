import base_types
import Max35Text
import ISODateTime
import GenericIdentification177
import Max6Text

class Traceability8(base_types._BaseFieldType):

	__slots__ = ["_PrtcolVrsn", "_PrtcolNm", "_TracDtTmIn", "_TracDtTmOut", "_RlayId"]
	@property
	def PrtcolVrsn(self):
		return self._PrtcolVrsn

	@PrtcolVrsn.setter
	def PrtcolVrsn(self, value):
		self._PrtcolVrsn = value if type(value) != auto else self.make_default("PrtcolVrsn")

	@PrtcolVrsn.deleter
	def PrtcolVrsn(self):
		del self._PrtcolVrsn
		self._PrtcolVrsn = None

	@property
	def PrtcolNm(self):
		return self._PrtcolNm

	@PrtcolNm.setter
	def PrtcolNm(self, value):
		self._PrtcolNm = value if type(value) != auto else self.make_default("PrtcolNm")

	@PrtcolNm.deleter
	def PrtcolNm(self):
		del self._PrtcolNm
		self._PrtcolNm = None

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
	def RlayId(self):
		return self._RlayId

	@RlayId.setter
	def RlayId(self, value):
		self._RlayId = value if type(value) != auto else self.make_default("RlayId")

	@RlayId.deleter
	def RlayId(self):
		del self._RlayId
		self._RlayId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtcolVrsn', type=Max6Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcolNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TracDtTmIn', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TracDtTmOut', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RlayId', type=GenericIdentification177, min=1, max=1, mutex_group=None, array=False),
	))

