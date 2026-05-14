# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Address4 import Address4
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._Max99Text import Max99Text

class HiredVehicle4(base_types._BaseFieldType):

	__slots__ = ["_CpnyNm", "_CpnyTp", "_DrvrId", "_DrvrTaxId", "_DstnAdr", "_DstnNmAndLctn", "_TpOfVhcl", "_VhclId"]
	@property
	def CpnyNm(self):
		return self._CpnyNm

	@CpnyNm.setter
	def CpnyNm(self, value):
		self._CpnyNm = value if type(value) != base_types.auto else self.make_default("CpnyNm")

	@CpnyNm.deleter
	def CpnyNm(self):
		del self._CpnyNm
		self._CpnyNm = None

	@property
	def CpnyTp(self):
		return self._CpnyTp

	@CpnyTp.setter
	def CpnyTp(self, value):
		self._CpnyTp = value if type(value) != base_types.auto else self.make_default("CpnyTp")

	@CpnyTp.deleter
	def CpnyTp(self):
		del self._CpnyTp
		self._CpnyTp = None

	@property
	def DrvrId(self):
		return self._DrvrId

	@DrvrId.setter
	def DrvrId(self, value):
		self._DrvrId = value if type(value) != base_types.auto else self.make_default("DrvrId")

	@DrvrId.deleter
	def DrvrId(self):
		del self._DrvrId
		self._DrvrId = None

	@property
	def DrvrTaxId(self):
		return self._DrvrTaxId

	@DrvrTaxId.setter
	def DrvrTaxId(self, value):
		self._DrvrTaxId = value if type(value) != base_types.auto else self.make_default("DrvrTaxId")

	@DrvrTaxId.deleter
	def DrvrTaxId(self):
		del self._DrvrTaxId
		self._DrvrTaxId = None

	@property
	def DstnAdr(self):
		return self._DstnAdr

	@DstnAdr.setter
	def DstnAdr(self, value):
		self._DstnAdr = value if type(value) != base_types.auto else self.make_default("DstnAdr")

	@DstnAdr.deleter
	def DstnAdr(self):
		del self._DstnAdr
		self._DstnAdr = None

	@property
	def DstnNmAndLctn(self):
		return self._DstnNmAndLctn

	@DstnNmAndLctn.setter
	def DstnNmAndLctn(self, value):
		self._DstnNmAndLctn = value if type(value) != base_types.auto else self.make_default("DstnNmAndLctn")

	@DstnNmAndLctn.deleter
	def DstnNmAndLctn(self):
		del self._DstnNmAndLctn
		self._DstnNmAndLctn = None

	@property
	def TpOfVhcl(self):
		return self._TpOfVhcl

	@TpOfVhcl.setter
	def TpOfVhcl(self, value):
		self._TpOfVhcl = value if type(value) != base_types.auto else self.make_default("TpOfVhcl")

	@TpOfVhcl.deleter
	def TpOfVhcl(self):
		del self._TpOfVhcl
		self._TpOfVhcl = None

	@property
	def VhclId(self):
		return self._VhclId

	@VhclId.setter
	def VhclId(self, value):
		self._VhclId = value if type(value) != base_types.auto else self.make_default("VhclId")

	@VhclId.deleter
	def VhclId(self):
		del self._VhclId
		self._VhclId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CpnyNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrTaxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnAdr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnNmAndLctn', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfVhcl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VhclId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))