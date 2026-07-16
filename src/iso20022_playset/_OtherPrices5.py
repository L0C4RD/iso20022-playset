# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Price14
from . import PriceInformation28

class OtherPrices5(base_types._BaseFieldType):

	__slots__ = ["_AllMktsWghtdAvrg", "_Bchmk", "_BchmkWghtdAvrg", "_IndxPric", "_Max", "_MktBrkrComssn", "_MrkdDwn", "_MrkdUp", "_NetDscld", "_NetUdscld", "_NtnlGrss", "_OthrPric", "_RefPric", "_RptdPric", "_Tx"]
	@property
	def AllMktsWghtdAvrg(self):
		return self._AllMktsWghtdAvrg

	@AllMktsWghtdAvrg.setter
	def AllMktsWghtdAvrg(self, value):
		self._AllMktsWghtdAvrg = value if value is not None else base_types.UninitialisedField(self, 'AllMktsWghtdAvrg', Price14, False)

	@AllMktsWghtdAvrg.deleter
	def AllMktsWghtdAvrg(self):
		del self._AllMktsWghtdAvrg
		self._AllMktsWghtdAvrg = base_types.UninitialisedField(self, 'AllMktsWghtdAvrg', Price14, False)

	@property
	def Bchmk(self):
		return self._Bchmk

	@Bchmk.setter
	def Bchmk(self, value):
		self._Bchmk = value if value is not None else base_types.UninitialisedField(self, 'Bchmk', Price14, False)

	@Bchmk.deleter
	def Bchmk(self):
		del self._Bchmk
		self._Bchmk = base_types.UninitialisedField(self, 'Bchmk', Price14, False)

	@property
	def BchmkWghtdAvrg(self):
		return self._BchmkWghtdAvrg

	@BchmkWghtdAvrg.setter
	def BchmkWghtdAvrg(self, value):
		self._BchmkWghtdAvrg = value if value is not None else base_types.UninitialisedField(self, 'BchmkWghtdAvrg', Price14, False)

	@BchmkWghtdAvrg.deleter
	def BchmkWghtdAvrg(self):
		del self._BchmkWghtdAvrg
		self._BchmkWghtdAvrg = base_types.UninitialisedField(self, 'BchmkWghtdAvrg', Price14, False)

	@property
	def IndxPric(self):
		return self._IndxPric

	@IndxPric.setter
	def IndxPric(self, value):
		self._IndxPric = value if value is not None else base_types.UninitialisedField(self, 'IndxPric', Price14, False)

	@IndxPric.deleter
	def IndxPric(self):
		del self._IndxPric
		self._IndxPric = base_types.UninitialisedField(self, 'IndxPric', Price14, False)

	@property
	def Max(self):
		return self._Max

	@Max.setter
	def Max(self, value):
		self._Max = value if value is not None else base_types.UninitialisedField(self, 'Max', Price14, False)

	@Max.deleter
	def Max(self):
		del self._Max
		self._Max = base_types.UninitialisedField(self, 'Max', Price14, False)

	@property
	def MktBrkrComssn(self):
		return self._MktBrkrComssn

	@MktBrkrComssn.setter
	def MktBrkrComssn(self, value):
		self._MktBrkrComssn = value if value is not None else base_types.UninitialisedField(self, 'MktBrkrComssn', Price14, False)

	@MktBrkrComssn.deleter
	def MktBrkrComssn(self):
		del self._MktBrkrComssn
		self._MktBrkrComssn = base_types.UninitialisedField(self, 'MktBrkrComssn', Price14, False)

	@property
	def MrkdDwn(self):
		return self._MrkdDwn

	@MrkdDwn.setter
	def MrkdDwn(self, value):
		self._MrkdDwn = value if value is not None else base_types.UninitialisedField(self, 'MrkdDwn', Price14, False)

	@MrkdDwn.deleter
	def MrkdDwn(self):
		del self._MrkdDwn
		self._MrkdDwn = base_types.UninitialisedField(self, 'MrkdDwn', Price14, False)

	@property
	def MrkdUp(self):
		return self._MrkdUp

	@MrkdUp.setter
	def MrkdUp(self, value):
		self._MrkdUp = value if value is not None else base_types.UninitialisedField(self, 'MrkdUp', Price14, False)

	@MrkdUp.deleter
	def MrkdUp(self):
		del self._MrkdUp
		self._MrkdUp = base_types.UninitialisedField(self, 'MrkdUp', Price14, False)

	@property
	def NetDscld(self):
		return self._NetDscld

	@NetDscld.setter
	def NetDscld(self, value):
		self._NetDscld = value if value is not None else base_types.UninitialisedField(self, 'NetDscld', Price14, False)

	@NetDscld.deleter
	def NetDscld(self):
		del self._NetDscld
		self._NetDscld = base_types.UninitialisedField(self, 'NetDscld', Price14, False)

	@property
	def NetUdscld(self):
		return self._NetUdscld

	@NetUdscld.setter
	def NetUdscld(self, value):
		self._NetUdscld = value if value is not None else base_types.UninitialisedField(self, 'NetUdscld', Price14, False)

	@NetUdscld.deleter
	def NetUdscld(self):
		del self._NetUdscld
		self._NetUdscld = base_types.UninitialisedField(self, 'NetUdscld', Price14, False)

	@property
	def NtnlGrss(self):
		return self._NtnlGrss

	@NtnlGrss.setter
	def NtnlGrss(self, value):
		self._NtnlGrss = value if value is not None else base_types.UninitialisedField(self, 'NtnlGrss', Price14, False)

	@NtnlGrss.deleter
	def NtnlGrss(self):
		del self._NtnlGrss
		self._NtnlGrss = base_types.UninitialisedField(self, 'NtnlGrss', Price14, False)

	@property
	def OthrPric(self):
		return self._OthrPric

	@OthrPric.setter
	def OthrPric(self, value):
		self._OthrPric = value if value is not None else base_types.UninitialisedField(self, 'OthrPric', Price14, False)

	@OthrPric.deleter
	def OthrPric(self):
		del self._OthrPric
		self._OthrPric = base_types.UninitialisedField(self, 'OthrPric', Price14, False)

	@property
	def RefPric(self):
		return self._RefPric

	@RefPric.setter
	def RefPric(self, value):
		self._RefPric = value if value is not None else base_types.UninitialisedField(self, 'RefPric', PriceInformation28, False)

	@RefPric.deleter
	def RefPric(self):
		del self._RefPric
		self._RefPric = base_types.UninitialisedField(self, 'RefPric', PriceInformation28, False)

	@property
	def RptdPric(self):
		return self._RptdPric

	@RptdPric.setter
	def RptdPric(self, value):
		self._RptdPric = value if value is not None else base_types.UninitialisedField(self, 'RptdPric', Price14, False)

	@RptdPric.deleter
	def RptdPric(self):
		del self._RptdPric
		self._RptdPric = base_types.UninitialisedField(self, 'RptdPric', Price14, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', Price14, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', Price14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllMktsWghtdAvrg', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bchmk', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkWghtdAvrg', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Max', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktBrkrComssn', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrkdDwn', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrkdUp', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetDscld', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetUdscld', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlGrss', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefPric', type=PriceInformation28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptdPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=Price14, min=0, max=1, mutex_group=None, array=False),
	))