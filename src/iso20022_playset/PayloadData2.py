import base_types
import Max35Text
import TrueFalseIndicator
import ISODateTime

class PayloadData2(base_types._BaseFieldType):

	__slots__ = ["_PyldIdr", "_CreDtAndTm", "_PssblDplctFlg"]
	@property
	def PyldIdr(self):
		return self._PyldIdr

	@PyldIdr.setter
	def PyldIdr(self, value):
		self._PyldIdr = value if type(value) != auto else self.make_default("PyldIdr")

	@PyldIdr.deleter
	def PyldIdr(self):
		del self._PyldIdr
		self._PyldIdr = None

	@property
	def CreDtAndTm(self):
		return self._CreDtAndTm

	@CreDtAndTm.setter
	def CreDtAndTm(self, value):
		self._CreDtAndTm = value if type(value) != auto else self.make_default("CreDtAndTm")

	@CreDtAndTm.deleter
	def CreDtAndTm(self):
		del self._CreDtAndTm
		self._CreDtAndTm = None

	@property
	def PssblDplctFlg(self):
		return self._PssblDplctFlg

	@PssblDplctFlg.setter
	def PssblDplctFlg(self, value):
		self._PssblDplctFlg = value if type(value) != auto else self.make_default("PssblDplctFlg")

	@PssblDplctFlg.deleter
	def PssblDplctFlg(self):
		del self._PssblDplctFlg
		self._PssblDplctFlg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PyldIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtAndTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PssblDplctFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

