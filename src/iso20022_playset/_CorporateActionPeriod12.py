# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Period6Choice

class CorporateActionPeriod12(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcrRvcbltyPrd", "_ActnPrd", "_DpstrySspnsnPrdForWdrwl", "_ParllTradgPrd", "_PricClctnPrd", "_PrvlgSspnsnPrd", "_RvcbltyPrd"]
	@property
	def AcctSvcrRvcbltyPrd(self):
		return self._AcctSvcrRvcbltyPrd

	@AcctSvcrRvcbltyPrd.setter
	def AcctSvcrRvcbltyPrd(self, value):
		self._AcctSvcrRvcbltyPrd = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrRvcbltyPrd', Period6Choice, False)

	@AcctSvcrRvcbltyPrd.deleter
	def AcctSvcrRvcbltyPrd(self):
		del self._AcctSvcrRvcbltyPrd
		self._AcctSvcrRvcbltyPrd = base_types.UninitialisedField(self, 'AcctSvcrRvcbltyPrd', Period6Choice, False)

	@property
	def ActnPrd(self):
		return self._ActnPrd

	@ActnPrd.setter
	def ActnPrd(self, value):
		self._ActnPrd = value if value is not None else base_types.UninitialisedField(self, 'ActnPrd', Period6Choice, False)

	@ActnPrd.deleter
	def ActnPrd(self):
		del self._ActnPrd
		self._ActnPrd = base_types.UninitialisedField(self, 'ActnPrd', Period6Choice, False)

	@property
	def DpstrySspnsnPrdForWdrwl(self):
		return self._DpstrySspnsnPrdForWdrwl

	@DpstrySspnsnPrdForWdrwl.setter
	def DpstrySspnsnPrdForWdrwl(self, value):
		self._DpstrySspnsnPrdForWdrwl = value if value is not None else base_types.UninitialisedField(self, 'DpstrySspnsnPrdForWdrwl', Period6Choice, False)

	@DpstrySspnsnPrdForWdrwl.deleter
	def DpstrySspnsnPrdForWdrwl(self):
		del self._DpstrySspnsnPrdForWdrwl
		self._DpstrySspnsnPrdForWdrwl = base_types.UninitialisedField(self, 'DpstrySspnsnPrdForWdrwl', Period6Choice, False)

	@property
	def ParllTradgPrd(self):
		return self._ParllTradgPrd

	@ParllTradgPrd.setter
	def ParllTradgPrd(self, value):
		self._ParllTradgPrd = value if value is not None else base_types.UninitialisedField(self, 'ParllTradgPrd', Period6Choice, False)

	@ParllTradgPrd.deleter
	def ParllTradgPrd(self):
		del self._ParllTradgPrd
		self._ParllTradgPrd = base_types.UninitialisedField(self, 'ParllTradgPrd', Period6Choice, False)

	@property
	def PricClctnPrd(self):
		return self._PricClctnPrd

	@PricClctnPrd.setter
	def PricClctnPrd(self, value):
		self._PricClctnPrd = value if value is not None else base_types.UninitialisedField(self, 'PricClctnPrd', Period6Choice, False)

	@PricClctnPrd.deleter
	def PricClctnPrd(self):
		del self._PricClctnPrd
		self._PricClctnPrd = base_types.UninitialisedField(self, 'PricClctnPrd', Period6Choice, False)

	@property
	def PrvlgSspnsnPrd(self):
		return self._PrvlgSspnsnPrd

	@PrvlgSspnsnPrd.setter
	def PrvlgSspnsnPrd(self, value):
		self._PrvlgSspnsnPrd = value if value is not None else base_types.UninitialisedField(self, 'PrvlgSspnsnPrd', Period6Choice, False)

	@PrvlgSspnsnPrd.deleter
	def PrvlgSspnsnPrd(self):
		del self._PrvlgSspnsnPrd
		self._PrvlgSspnsnPrd = base_types.UninitialisedField(self, 'PrvlgSspnsnPrd', Period6Choice, False)

	@property
	def RvcbltyPrd(self):
		return self._RvcbltyPrd

	@RvcbltyPrd.setter
	def RvcbltyPrd(self, value):
		self._RvcbltyPrd = value if value is not None else base_types.UninitialisedField(self, 'RvcbltyPrd', Period6Choice, False)

	@RvcbltyPrd.deleter
	def RvcbltyPrd(self):
		del self._RvcbltyPrd
		self._RvcbltyPrd = base_types.UninitialisedField(self, 'RvcbltyPrd', Period6Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSvcrRvcbltyPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForWdrwl', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ParllTradgPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricClctnPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvlgSspnsnPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvcbltyPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
	))