# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashMovement2
from . import CorporateActionMovement1
from . import ProceedsMovement1
from . import UnderlyingSecurityMovement1

class MovementInstruction1(base_types._BaseFieldType):

	__slots__ = ["_MvmntGnlInf", "_PrcdsMvmntDtls", "_UndrlygCshMvmntDtls", "_UndrlygSctiesMvmntDtls"]
	@property
	def MvmntGnlInf(self):
		return self._MvmntGnlInf

	@MvmntGnlInf.setter
	def MvmntGnlInf(self, value):
		self._MvmntGnlInf = value if value is not None else base_types.UninitialisedField(self, 'MvmntGnlInf', CorporateActionMovement1, False)

	@MvmntGnlInf.deleter
	def MvmntGnlInf(self):
		del self._MvmntGnlInf
		self._MvmntGnlInf = base_types.UninitialisedField(self, 'MvmntGnlInf', CorporateActionMovement1, False)

	@property
	def PrcdsMvmntDtls(self):
		return self._PrcdsMvmntDtls

	@PrcdsMvmntDtls.setter
	def PrcdsMvmntDtls(self, value):
		self._PrcdsMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'PrcdsMvmntDtls', ProceedsMovement1, True)

	@PrcdsMvmntDtls.deleter
	def PrcdsMvmntDtls(self):
		del self._PrcdsMvmntDtls
		self._PrcdsMvmntDtls = base_types.UninitialisedField(self, 'PrcdsMvmntDtls', ProceedsMovement1, True)

	@property
	def UndrlygCshMvmntDtls(self):
		return self._UndrlygCshMvmntDtls

	@UndrlygCshMvmntDtls.setter
	def UndrlygCshMvmntDtls(self, value):
		self._UndrlygCshMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'UndrlygCshMvmntDtls', CashMovement2, True)

	@UndrlygCshMvmntDtls.deleter
	def UndrlygCshMvmntDtls(self):
		del self._UndrlygCshMvmntDtls
		self._UndrlygCshMvmntDtls = base_types.UninitialisedField(self, 'UndrlygCshMvmntDtls', CashMovement2, True)

	@property
	def UndrlygSctiesMvmntDtls(self):
		return self._UndrlygSctiesMvmntDtls

	@UndrlygSctiesMvmntDtls.setter
	def UndrlygSctiesMvmntDtls(self, value):
		self._UndrlygSctiesMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'UndrlygSctiesMvmntDtls', UnderlyingSecurityMovement1, True)

	@UndrlygSctiesMvmntDtls.deleter
	def UndrlygSctiesMvmntDtls(self):
		del self._UndrlygSctiesMvmntDtls
		self._UndrlygSctiesMvmntDtls = base_types.UninitialisedField(self, 'UndrlygSctiesMvmntDtls', UnderlyingSecurityMovement1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MvmntGnlInf', type=CorporateActionMovement1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcdsMvmntDtls', type=ProceedsMovement1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygCshMvmntDtls', type=CashMovement2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygSctiesMvmntDtls', type=UnderlyingSecurityMovement1, min=0, max=None, mutex_group=None, array=True),
	))