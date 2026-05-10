import base_types
import CashMovement2
import ProceedsMovement1
import UnderlyingSecurityMovement1
import CorporateActionMovement1

class MovementInstruction1(base_types._BaseFieldType):

	__slots__ = ["_MvmntGnlInf", "_PrcdsMvmntDtls", "_UndrlygSctiesMvmntDtls", "_UndrlygCshMvmntDtls"]
	@property
	def MvmntGnlInf(self):
		return self._MvmntGnlInf

	@MvmntGnlInf.setter
	def MvmntGnlInf(self, value):
		self._MvmntGnlInf = value if type(value) != auto else self.make_default("MvmntGnlInf")

	@MvmntGnlInf.deleter
	def MvmntGnlInf(self):
		del self._MvmntGnlInf
		self._MvmntGnlInf = None

	@property
	def PrcdsMvmntDtls(self):
		return self._PrcdsMvmntDtls

	@PrcdsMvmntDtls.setter
	def PrcdsMvmntDtls(self, value):
		self._PrcdsMvmntDtls = value if type(value) != auto else self.make_default("PrcdsMvmntDtls")

	@PrcdsMvmntDtls.deleter
	def PrcdsMvmntDtls(self):
		del self._PrcdsMvmntDtls
		self._PrcdsMvmntDtls = None

	@property
	def UndrlygSctiesMvmntDtls(self):
		return self._UndrlygSctiesMvmntDtls

	@UndrlygSctiesMvmntDtls.setter
	def UndrlygSctiesMvmntDtls(self, value):
		self._UndrlygSctiesMvmntDtls = value if type(value) != auto else self.make_default("UndrlygSctiesMvmntDtls")

	@UndrlygSctiesMvmntDtls.deleter
	def UndrlygSctiesMvmntDtls(self):
		del self._UndrlygSctiesMvmntDtls
		self._UndrlygSctiesMvmntDtls = None

	@property
	def UndrlygCshMvmntDtls(self):
		return self._UndrlygCshMvmntDtls

	@UndrlygCshMvmntDtls.setter
	def UndrlygCshMvmntDtls(self, value):
		self._UndrlygCshMvmntDtls = value if type(value) != auto else self.make_default("UndrlygCshMvmntDtls")

	@UndrlygCshMvmntDtls.deleter
	def UndrlygCshMvmntDtls(self):
		del self._UndrlygCshMvmntDtls
		self._UndrlygCshMvmntDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MvmntGnlInf', type=CorporateActionMovement1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcdsMvmntDtls', type=ProceedsMovement1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygSctiesMvmntDtls', type=UnderlyingSecurityMovement1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygCshMvmntDtls', type=CashMovement2, min=0, max=None, mutex_group=None, array=True),
	))

