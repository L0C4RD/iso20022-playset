# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalEffectiveDateParameter1Code
from . import ISODate

class EffectiveDate1(base_types._BaseFieldType):

	__slots__ = ["_FctvDt", "_FctvDtParam"]
	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if value is not None else base_types.UninitialisedField(self, 'FctvDt', ISODate, False)

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = base_types.UninitialisedField(self, 'FctvDt', ISODate, False)

	@property
	def FctvDtParam(self):
		return self._FctvDtParam

	@FctvDtParam.setter
	def FctvDtParam(self, value):
		self._FctvDtParam = value if value is not None else base_types.UninitialisedField(self, 'FctvDtParam', ExternalEffectiveDateParameter1Code, False)

	@FctvDtParam.deleter
	def FctvDtParam(self):
		del self._FctvDtParam
		self._FctvDtParam = base_types.UninitialisedField(self, 'FctvDtParam', ExternalEffectiveDateParameter1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FctvDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDtParam', type=ExternalEffectiveDateParameter1Code, min=0, max=1, mutex_group=None, array=False),
	))