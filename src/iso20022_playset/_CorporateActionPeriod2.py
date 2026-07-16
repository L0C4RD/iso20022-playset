# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Period1

class CorporateActionPeriod2(base_types._BaseFieldType):

	__slots__ = ["_ActnPrd", "_AssntdLinePrd", "_ParllTradgPrd", "_PricClctnPrd", "_PrvlgSspnsnPrd", "_RvcbltyPrd", "_SellThruIssrPrd"]
	@property
	def ActnPrd(self):
		return self._ActnPrd

	@ActnPrd.setter
	def ActnPrd(self, value):
		self._ActnPrd = value if value is not None else base_types.UninitialisedField(self, 'ActnPrd', Period1, False)

	@ActnPrd.deleter
	def ActnPrd(self):
		del self._ActnPrd
		self._ActnPrd = base_types.UninitialisedField(self, 'ActnPrd', Period1, False)

	@property
	def AssntdLinePrd(self):
		return self._AssntdLinePrd

	@AssntdLinePrd.setter
	def AssntdLinePrd(self, value):
		self._AssntdLinePrd = value if value is not None else base_types.UninitialisedField(self, 'AssntdLinePrd', Period1, False)

	@AssntdLinePrd.deleter
	def AssntdLinePrd(self):
		del self._AssntdLinePrd
		self._AssntdLinePrd = base_types.UninitialisedField(self, 'AssntdLinePrd', Period1, False)

	@property
	def ParllTradgPrd(self):
		return self._ParllTradgPrd

	@ParllTradgPrd.setter
	def ParllTradgPrd(self, value):
		self._ParllTradgPrd = value if value is not None else base_types.UninitialisedField(self, 'ParllTradgPrd', Period1, False)

	@ParllTradgPrd.deleter
	def ParllTradgPrd(self):
		del self._ParllTradgPrd
		self._ParllTradgPrd = base_types.UninitialisedField(self, 'ParllTradgPrd', Period1, False)

	@property
	def PricClctnPrd(self):
		return self._PricClctnPrd

	@PricClctnPrd.setter
	def PricClctnPrd(self, value):
		self._PricClctnPrd = value if value is not None else base_types.UninitialisedField(self, 'PricClctnPrd', Period1, False)

	@PricClctnPrd.deleter
	def PricClctnPrd(self):
		del self._PricClctnPrd
		self._PricClctnPrd = base_types.UninitialisedField(self, 'PricClctnPrd', Period1, False)

	@property
	def PrvlgSspnsnPrd(self):
		return self._PrvlgSspnsnPrd

	@PrvlgSspnsnPrd.setter
	def PrvlgSspnsnPrd(self, value):
		self._PrvlgSspnsnPrd = value if value is not None else base_types.UninitialisedField(self, 'PrvlgSspnsnPrd', Period1, False)

	@PrvlgSspnsnPrd.deleter
	def PrvlgSspnsnPrd(self):
		del self._PrvlgSspnsnPrd
		self._PrvlgSspnsnPrd = base_types.UninitialisedField(self, 'PrvlgSspnsnPrd', Period1, False)

	@property
	def RvcbltyPrd(self):
		return self._RvcbltyPrd

	@RvcbltyPrd.setter
	def RvcbltyPrd(self, value):
		self._RvcbltyPrd = value if value is not None else base_types.UninitialisedField(self, 'RvcbltyPrd', Period1, False)

	@RvcbltyPrd.deleter
	def RvcbltyPrd(self):
		del self._RvcbltyPrd
		self._RvcbltyPrd = base_types.UninitialisedField(self, 'RvcbltyPrd', Period1, False)

	@property
	def SellThruIssrPrd(self):
		return self._SellThruIssrPrd

	@SellThruIssrPrd.setter
	def SellThruIssrPrd(self, value):
		self._SellThruIssrPrd = value if value is not None else base_types.UninitialisedField(self, 'SellThruIssrPrd', Period1, False)

	@SellThruIssrPrd.deleter
	def SellThruIssrPrd(self):
		del self._SellThruIssrPrd
		self._SellThruIssrPrd = base_types.UninitialisedField(self, 'SellThruIssrPrd', Period1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssntdLinePrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ParllTradgPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricClctnPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvlgSspnsnPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvcbltyPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellThruIssrPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
	))