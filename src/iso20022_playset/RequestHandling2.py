from . import base_types
import Max4AlphaNumericText
import Max140Text
import ISODateTime

class RequestHandling2(base_types._BaseFieldType):

	__slots__ = ["_StsCd", "_StsDtTm", "_Desc"]
	@property
	def StsCd(self):
		return self._StsCd

	@StsCd.setter
	def StsCd(self, value):
		self._StsCd = value if type(value) != auto else self.make_default("StsCd")

	@StsCd.deleter
	def StsCd(self):
		del self._StsCd
		self._StsCd = None

	@property
	def StsDtTm(self):
		return self._StsDtTm

	@StsDtTm.setter
	def StsDtTm(self, value):
		self._StsDtTm = value if type(value) != auto else self.make_default("StsDtTm")

	@StsDtTm.deleter
	def StsDtTm(self):
		del self._StsDtTm
		self._StsDtTm = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsCd', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

