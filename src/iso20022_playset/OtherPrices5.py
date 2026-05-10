import base_types
import Price14
import PriceInformation28

class OtherPrices5(base_types._BaseFieldType):

	__slots__ = ["_IndxPric", "_Max", "_NetUdscld", "_OthrPric", "_Tx", "_NetDscld", "_RefPric", "_RptdPric", "_MrkdDwn", "_AllMktsWghtdAvrg", "_MrkdUp", "_NtnlGrss", "_MktBrkrComssn", "_Bchmk", "_BchmkWghtdAvrg"]
	@property
	def IndxPric(self):
		return self._IndxPric

	@IndxPric.setter
	def IndxPric(self, value):
		self._IndxPric = value if type(value) != auto else self.make_default("IndxPric")

	@IndxPric.deleter
	def IndxPric(self):
		del self._IndxPric
		self._IndxPric = None

	@property
	def Max(self):
		return self._Max

	@Max.setter
	def Max(self, value):
		self._Max = value if type(value) != auto else self.make_default("Max")

	@Max.deleter
	def Max(self):
		del self._Max
		self._Max = None

	@property
	def NetUdscld(self):
		return self._NetUdscld

	@NetUdscld.setter
	def NetUdscld(self, value):
		self._NetUdscld = value if type(value) != auto else self.make_default("NetUdscld")

	@NetUdscld.deleter
	def NetUdscld(self):
		del self._NetUdscld
		self._NetUdscld = None

	@property
	def OthrPric(self):
		return self._OthrPric

	@OthrPric.setter
	def OthrPric(self, value):
		self._OthrPric = value if type(value) != auto else self.make_default("OthrPric")

	@OthrPric.deleter
	def OthrPric(self):
		del self._OthrPric
		self._OthrPric = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	@property
	def NetDscld(self):
		return self._NetDscld

	@NetDscld.setter
	def NetDscld(self, value):
		self._NetDscld = value if type(value) != auto else self.make_default("NetDscld")

	@NetDscld.deleter
	def NetDscld(self):
		del self._NetDscld
		self._NetDscld = None

	@property
	def RefPric(self):
		return self._RefPric

	@RefPric.setter
	def RefPric(self, value):
		self._RefPric = value if type(value) != auto else self.make_default("RefPric")

	@RefPric.deleter
	def RefPric(self):
		del self._RefPric
		self._RefPric = None

	@property
	def RptdPric(self):
		return self._RptdPric

	@RptdPric.setter
	def RptdPric(self, value):
		self._RptdPric = value if type(value) != auto else self.make_default("RptdPric")

	@RptdPric.deleter
	def RptdPric(self):
		del self._RptdPric
		self._RptdPric = None

	@property
	def MrkdDwn(self):
		return self._MrkdDwn

	@MrkdDwn.setter
	def MrkdDwn(self, value):
		self._MrkdDwn = value if type(value) != auto else self.make_default("MrkdDwn")

	@MrkdDwn.deleter
	def MrkdDwn(self):
		del self._MrkdDwn
		self._MrkdDwn = None

	@property
	def AllMktsWghtdAvrg(self):
		return self._AllMktsWghtdAvrg

	@AllMktsWghtdAvrg.setter
	def AllMktsWghtdAvrg(self, value):
		self._AllMktsWghtdAvrg = value if type(value) != auto else self.make_default("AllMktsWghtdAvrg")

	@AllMktsWghtdAvrg.deleter
	def AllMktsWghtdAvrg(self):
		del self._AllMktsWghtdAvrg
		self._AllMktsWghtdAvrg = None

	@property
	def MrkdUp(self):
		return self._MrkdUp

	@MrkdUp.setter
	def MrkdUp(self, value):
		self._MrkdUp = value if type(value) != auto else self.make_default("MrkdUp")

	@MrkdUp.deleter
	def MrkdUp(self):
		del self._MrkdUp
		self._MrkdUp = None

	@property
	def NtnlGrss(self):
		return self._NtnlGrss

	@NtnlGrss.setter
	def NtnlGrss(self, value):
		self._NtnlGrss = value if type(value) != auto else self.make_default("NtnlGrss")

	@NtnlGrss.deleter
	def NtnlGrss(self):
		del self._NtnlGrss
		self._NtnlGrss = None

	@property
	def MktBrkrComssn(self):
		return self._MktBrkrComssn

	@MktBrkrComssn.setter
	def MktBrkrComssn(self, value):
		self._MktBrkrComssn = value if type(value) != auto else self.make_default("MktBrkrComssn")

	@MktBrkrComssn.deleter
	def MktBrkrComssn(self):
		del self._MktBrkrComssn
		self._MktBrkrComssn = None

	@property
	def Bchmk(self):
		return self._Bchmk

	@Bchmk.setter
	def Bchmk(self, value):
		self._Bchmk = value if type(value) != auto else self.make_default("Bchmk")

	@Bchmk.deleter
	def Bchmk(self):
		del self._Bchmk
		self._Bchmk = None

	@property
	def BchmkWghtdAvrg(self):
		return self._BchmkWghtdAvrg

	@BchmkWghtdAvrg.setter
	def BchmkWghtdAvrg(self, value):
		self._BchmkWghtdAvrg = value if type(value) != auto else self.make_default("BchmkWghtdAvrg")

	@BchmkWghtdAvrg.deleter
	def BchmkWghtdAvrg(self):
		del self._BchmkWghtdAvrg
		self._BchmkWghtdAvrg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndxPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Max', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetUdscld', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetDscld', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefPric', type=PriceInformation28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptdPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrkdDwn', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllMktsWghtdAvrg', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrkdUp', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlGrss', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktBrkrComssn', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bchmk', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkWghtdAvrg', type=Price14, min=0, max=1, mutex_group=None, array=False),
	))

