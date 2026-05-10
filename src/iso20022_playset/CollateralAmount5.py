import base_types
import AmountAndDirection44

class CollateralAmount5(base_types._BaseFieldType):

	__slots__ = ["_Collsd", "_Sttld", "_RmngCollsd", "_RmngSttlm", "_ReqrdMrgn"]
	@property
	def Collsd(self):
		return self._Collsd

	@Collsd.setter
	def Collsd(self, value):
		self._Collsd = value if type(value) != auto else self.make_default("Collsd")

	@Collsd.deleter
	def Collsd(self):
		del self._Collsd
		self._Collsd = None

	@property
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if type(value) != auto else self.make_default("Sttld")

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = None

	@property
	def RmngCollsd(self):
		return self._RmngCollsd

	@RmngCollsd.setter
	def RmngCollsd(self, value):
		self._RmngCollsd = value if type(value) != auto else self.make_default("RmngCollsd")

	@RmngCollsd.deleter
	def RmngCollsd(self):
		del self._RmngCollsd
		self._RmngCollsd = None

	@property
	def RmngSttlm(self):
		return self._RmngSttlm

	@RmngSttlm.setter
	def RmngSttlm(self, value):
		self._RmngSttlm = value if type(value) != auto else self.make_default("RmngSttlm")

	@RmngSttlm.deleter
	def RmngSttlm(self):
		del self._RmngSttlm
		self._RmngSttlm = None

	@property
	def ReqrdMrgn(self):
		return self._ReqrdMrgn

	@ReqrdMrgn.setter
	def ReqrdMrgn(self, value):
		self._ReqrdMrgn = value if type(value) != auto else self.make_default("ReqrdMrgn")

	@ReqrdMrgn.deleter
	def ReqrdMrgn(self):
		del self._ReqrdMrgn
		self._ReqrdMrgn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Collsd', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttld', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngCollsd', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngSttlm', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdMrgn', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
	))

