# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashOption112
from . import CorporateActionOption39Choice
from . import OptionNumber1Choice
from . import SecuritiesOption86

class CorporateActionOption246(base_types._BaseFieldType):

	__slots__ = ["_CshMvmntDtls", "_OptnNb", "_OptnTp", "_SctiesMvmntDtls"]
	@property
	def CshMvmntDtls(self):
		return self._CshMvmntDtls

	@CshMvmntDtls.setter
	def CshMvmntDtls(self, value):
		self._CshMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'CshMvmntDtls', CashOption112, True)

	@CshMvmntDtls.deleter
	def CshMvmntDtls(self):
		del self._CshMvmntDtls
		self._CshMvmntDtls = base_types.UninitialisedField(self, 'CshMvmntDtls', CashOption112, True)

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if value is not None else base_types.UninitialisedField(self, 'OptnNb', OptionNumber1Choice, False)

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = base_types.UninitialisedField(self, 'OptnNb', OptionNumber1Choice, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption39Choice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption39Choice, False)

	@property
	def SctiesMvmntDtls(self):
		return self._SctiesMvmntDtls

	@SctiesMvmntDtls.setter
	def SctiesMvmntDtls(self, value):
		self._SctiesMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntDtls', SecuritiesOption86, True)

	@SctiesMvmntDtls.deleter
	def SctiesMvmntDtls(self):
		del self._SctiesMvmntDtls
		self._SctiesMvmntDtls = base_types.UninitialisedField(self, 'SctiesMvmntDtls', SecuritiesOption86, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshMvmntDtls', type=CashOption112, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnNb', type=OptionNumber1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption39Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntDtls', type=SecuritiesOption86, min=0, max=None, mutex_group=None, array=True),
	))