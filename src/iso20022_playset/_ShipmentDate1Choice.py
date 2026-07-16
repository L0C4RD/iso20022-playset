# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate

class ShipmentDate1Choice(base_types._BaseFieldType):

	__slots__ = ["_ActlShipmntDt", "_PropsdShipmntDt"]
	@property
	def ActlShipmntDt(self):
		return self._ActlShipmntDt

	@ActlShipmntDt.setter
	def ActlShipmntDt(self, value):
		self._ActlShipmntDt = value if value is not None else base_types.UninitialisedField(self, 'ActlShipmntDt', ISODate, False)

	@ActlShipmntDt.deleter
	def ActlShipmntDt(self):
		del self._ActlShipmntDt
		self._ActlShipmntDt = base_types.UninitialisedField(self, 'ActlShipmntDt', ISODate, False)

	@property
	def PropsdShipmntDt(self):
		return self._PropsdShipmntDt

	@PropsdShipmntDt.setter
	def PropsdShipmntDt(self, value):
		self._PropsdShipmntDt = value if value is not None else base_types.UninitialisedField(self, 'PropsdShipmntDt', ISODate, False)

	@PropsdShipmntDt.deleter
	def PropsdShipmntDt(self):
		del self._PropsdShipmntDt
		self._PropsdShipmntDt = base_types.UninitialisedField(self, 'PropsdShipmntDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActlShipmntDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PropsdShipmntDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
	))