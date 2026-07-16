# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Address4
from . import Max35Text
from . import Max70Text
from . import Max99Text

class HiredVehicle4(base_types._BaseFieldType):

	__slots__ = ["_CpnyNm", "_CpnyTp", "_DrvrId", "_DrvrTaxId", "_DstnAdr", "_DstnNmAndLctn", "_TpOfVhcl", "_VhclId"]
	@property
	def CpnyNm(self):
		return self._CpnyNm

	@CpnyNm.setter
	def CpnyNm(self, value):
		self._CpnyNm = value if value is not None else base_types.UninitialisedField(self, 'CpnyNm', Max70Text, False)

	@CpnyNm.deleter
	def CpnyNm(self):
		del self._CpnyNm
		self._CpnyNm = base_types.UninitialisedField(self, 'CpnyNm', Max70Text, False)

	@property
	def CpnyTp(self):
		return self._CpnyTp

	@CpnyTp.setter
	def CpnyTp(self, value):
		self._CpnyTp = value if value is not None else base_types.UninitialisedField(self, 'CpnyTp', Max35Text, False)

	@CpnyTp.deleter
	def CpnyTp(self):
		del self._CpnyTp
		self._CpnyTp = base_types.UninitialisedField(self, 'CpnyTp', Max35Text, False)

	@property
	def DrvrId(self):
		return self._DrvrId

	@DrvrId.setter
	def DrvrId(self, value):
		self._DrvrId = value if value is not None else base_types.UninitialisedField(self, 'DrvrId', Max35Text, False)

	@DrvrId.deleter
	def DrvrId(self):
		del self._DrvrId
		self._DrvrId = base_types.UninitialisedField(self, 'DrvrId', Max35Text, False)

	@property
	def DrvrTaxId(self):
		return self._DrvrTaxId

	@DrvrTaxId.setter
	def DrvrTaxId(self, value):
		self._DrvrTaxId = value if value is not None else base_types.UninitialisedField(self, 'DrvrTaxId', Max35Text, False)

	@DrvrTaxId.deleter
	def DrvrTaxId(self):
		del self._DrvrTaxId
		self._DrvrTaxId = base_types.UninitialisedField(self, 'DrvrTaxId', Max35Text, False)

	@property
	def DstnAdr(self):
		return self._DstnAdr

	@DstnAdr.setter
	def DstnAdr(self, value):
		self._DstnAdr = value if value is not None else base_types.UninitialisedField(self, 'DstnAdr', Address4, False)

	@DstnAdr.deleter
	def DstnAdr(self):
		del self._DstnAdr
		self._DstnAdr = base_types.UninitialisedField(self, 'DstnAdr', Address4, False)

	@property
	def DstnNmAndLctn(self):
		return self._DstnNmAndLctn

	@DstnNmAndLctn.setter
	def DstnNmAndLctn(self, value):
		self._DstnNmAndLctn = value if value is not None else base_types.UninitialisedField(self, 'DstnNmAndLctn', Max99Text, False)

	@DstnNmAndLctn.deleter
	def DstnNmAndLctn(self):
		del self._DstnNmAndLctn
		self._DstnNmAndLctn = base_types.UninitialisedField(self, 'DstnNmAndLctn', Max99Text, False)

	@property
	def TpOfVhcl(self):
		return self._TpOfVhcl

	@TpOfVhcl.setter
	def TpOfVhcl(self, value):
		self._TpOfVhcl = value if value is not None else base_types.UninitialisedField(self, 'TpOfVhcl', Max35Text, False)

	@TpOfVhcl.deleter
	def TpOfVhcl(self):
		del self._TpOfVhcl
		self._TpOfVhcl = base_types.UninitialisedField(self, 'TpOfVhcl', Max35Text, False)

	@property
	def VhclId(self):
		return self._VhclId

	@VhclId.setter
	def VhclId(self, value):
		self._VhclId = value if value is not None else base_types.UninitialisedField(self, 'VhclId', Max35Text, False)

	@VhclId.deleter
	def VhclId(self):
		del self._VhclId
		self._VhclId = base_types.UninitialisedField(self, 'VhclId', Max35Text, False)

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