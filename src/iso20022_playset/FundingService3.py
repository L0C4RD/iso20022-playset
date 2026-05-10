import base_types
import Max500Text
import Max256Text
import FundingSource4
import Max35Text

class FundingService3(base_types._BaseFieldType):

	__slots__ = ["_Nm", "_BizPurp", "_ClmCrdntls", "_ClmAssgnr", "_FndgSrc", "_Prvdr", "_Ref", "_Desc"]
	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def BizPurp(self):
		return self._BizPurp

	@BizPurp.setter
	def BizPurp(self, value):
		self._BizPurp = value if type(value) != auto else self.make_default("BizPurp")

	@BizPurp.deleter
	def BizPurp(self):
		del self._BizPurp
		self._BizPurp = None

	@property
	def ClmCrdntls(self):
		return self._ClmCrdntls

	@ClmCrdntls.setter
	def ClmCrdntls(self, value):
		self._ClmCrdntls = value if type(value) != auto else self.make_default("ClmCrdntls")

	@ClmCrdntls.deleter
	def ClmCrdntls(self):
		del self._ClmCrdntls
		self._ClmCrdntls = None

	@property
	def ClmAssgnr(self):
		return self._ClmAssgnr

	@ClmAssgnr.setter
	def ClmAssgnr(self, value):
		self._ClmAssgnr = value if type(value) != auto else self.make_default("ClmAssgnr")

	@ClmAssgnr.deleter
	def ClmAssgnr(self):
		del self._ClmAssgnr
		self._ClmAssgnr = None

	@property
	def FndgSrc(self):
		return self._FndgSrc

	@FndgSrc.setter
	def FndgSrc(self, value):
		self._FndgSrc = value if type(value) != auto else self.make_default("FndgSrc")

	@FndgSrc.deleter
	def FndgSrc(self):
		del self._FndgSrc
		self._FndgSrc = None

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if type(value) != auto else self.make_default("Prvdr")

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizPurp', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClmCrdntls', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClmAssgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndgSrc', type=FundingSource4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))

