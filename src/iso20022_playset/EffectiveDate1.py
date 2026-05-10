import base_types
import ISODate
import ExternalEffectiveDateParameter1Code

class EffectiveDate1(base_types._BaseFieldType):

	__slots__ = ["_FctvDt", "_FctvDtParam"]
	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if type(value) != auto else self.make_default("FctvDt")

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = None

	@property
	def FctvDtParam(self):
		return self._FctvDtParam

	@FctvDtParam.setter
	def FctvDtParam(self, value):
		self._FctvDtParam = value if type(value) != auto else self.make_default("FctvDtParam")

	@FctvDtParam.deleter
	def FctvDtParam(self):
		del self._FctvDtParam
		self._FctvDtParam = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FctvDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDtParam', type=ExternalEffectiveDateParameter1Code, min=0, max=1, mutex_group=None, array=False),
	))

