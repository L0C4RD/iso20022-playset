from . import base_types
from ._Max35Text import Max35Text
from ._TrueFalseIndicator import TrueFalseIndicator
from ._ISODateTime import ISODateTime

class PayloadData2(base_types._BaseFieldType):

	__slots__ = ["_PssblDplctFlg", "_CreDtAndTm", "_PyldIdr"]
	@property
	def PssblDplctFlg(self):
		return self._PssblDplctFlg

	@PssblDplctFlg.setter
	def PssblDplctFlg(self, value):
		self._PssblDplctFlg = value if type(value) != base_types.auto else self.make_default("PssblDplctFlg")

	@PssblDplctFlg.deleter
	def PssblDplctFlg(self):
		del self._PssblDplctFlg
		self._PssblDplctFlg = None

	@property
	def CreDtAndTm(self):
		return self._CreDtAndTm

	@CreDtAndTm.setter
	def CreDtAndTm(self, value):
		self._CreDtAndTm = value if type(value) != base_types.auto else self.make_default("CreDtAndTm")

	@CreDtAndTm.deleter
	def CreDtAndTm(self):
		del self._CreDtAndTm
		self._CreDtAndTm = None

	@property
	def PyldIdr(self):
		return self._PyldIdr

	@PyldIdr.setter
	def PyldIdr(self, value):
		self._PyldIdr = value if type(value) != base_types.auto else self.make_default("PyldIdr")

	@PyldIdr.deleter
	def PyldIdr(self):
		del self._PyldIdr
		self._PyldIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PssblDplctFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtAndTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyldIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

