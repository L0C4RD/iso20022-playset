# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Period11

class CorporateActionPeriod13(base_types._BaseFieldType):

	__slots__ = ["_ActnPrd", "_ParllTradgPrd", "_PricClctnPrd"]
	@property
	def ActnPrd(self):
		return self._ActnPrd

	@ActnPrd.setter
	def ActnPrd(self, value):
		self._ActnPrd = value if value is not None else base_types.UninitialisedField(self, 'ActnPrd', Period11, False)

	@ActnPrd.deleter
	def ActnPrd(self):
		del self._ActnPrd
		self._ActnPrd = base_types.UninitialisedField(self, 'ActnPrd', Period11, False)

	@property
	def ParllTradgPrd(self):
		return self._ParllTradgPrd

	@ParllTradgPrd.setter
	def ParllTradgPrd(self, value):
		self._ParllTradgPrd = value if value is not None else base_types.UninitialisedField(self, 'ParllTradgPrd', Period11, False)

	@ParllTradgPrd.deleter
	def ParllTradgPrd(self):
		del self._ParllTradgPrd
		self._ParllTradgPrd = base_types.UninitialisedField(self, 'ParllTradgPrd', Period11, False)

	@property
	def PricClctnPrd(self):
		return self._PricClctnPrd

	@PricClctnPrd.setter
	def PricClctnPrd(self, value):
		self._PricClctnPrd = value if value is not None else base_types.UninitialisedField(self, 'PricClctnPrd', Period11, False)

	@PricClctnPrd.deleter
	def PricClctnPrd(self):
		del self._PricClctnPrd
		self._PricClctnPrd = base_types.UninitialisedField(self, 'PricClctnPrd', Period11, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnPrd', type=Period11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ParllTradgPrd', type=Period11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricClctnPrd', type=Period11, min=0, max=1, mutex_group=None, array=False),
	))