from . import base_types
from .ContactAttributes5 import ContactAttributes5
from .ISODate import ISODate
from .AdditionalInformation15 import AdditionalInformation15

class OrderDesk1(base_types._BaseFieldType):

	__slots__ = ["_ClsrDts", "_AddtlInf", "_OrdrDsk"]
	@property
	def ClsrDts(self):
		return self._ClsrDts

	@ClsrDts.setter
	def ClsrDts(self, value):
		self._ClsrDts = value if type(value) != base_types.auto else self.make_default("ClsrDts")

	@ClsrDts.deleter
	def ClsrDts(self):
		del self._ClsrDts
		self._ClsrDts = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def OrdrDsk(self):
		return self._OrdrDsk

	@OrdrDsk.setter
	def OrdrDsk(self, value):
		self._OrdrDsk = value if type(value) != base_types.auto else self.make_default("OrdrDsk")

	@OrdrDsk.deleter
	def OrdrDsk(self):
		del self._OrdrDsk
		self._OrdrDsk = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsrDts', type=ISODate, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrdrDsk', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
	))

